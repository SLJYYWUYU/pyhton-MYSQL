import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from utils import *

from log_utils import audit_log

# 常量定义
MENU_WIDTH_RATIO = 0.15  # 左侧菜单宽度比例
WINDOW_SIZE = '1200x900+600+700'  # 窗口大小
TEXT_INDENT = 50  # 文本缩进
LINE_HEIGHT = 35  # 行高

class menu:
    def __init__(self, student_id):
        self.student_id = student_id
        self.root = tk.Tk()
        self.root.geometry(WINDOW_SIZE)
        self.root.title(f'学生')
        self.root.resizable(False, False)
        
        # 创建菜单
        self.create_menu()
        
        # 默认显示学生信息
        self.show_student_info()
        
    def create_menu(self):
        """创建左侧菜单栏"""
        self.menu_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.menu_frame.place(relheight=1, relwidth=MENU_WIDTH_RATIO)
        
        # 菜单按钮样式
        btn_style = {
            'font': ('Microsoft YaHei', 12),
            'relief': 'flat',
            'bg': '#e1e1e1',
            'activebackground': '#d1d1d1'
        }
        
        # 个人信息按钮
        tk.Button(
            self.menu_frame, 
            text='个人信息', 
            command=self.show_student_info,
            **btn_style
        ).place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.08)
        
        # 课程成绩按钮
        tk.Button(
            self.menu_frame, 
            text='课程成绩', 
            command=self.show_student_grades,
            **btn_style
        ).place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.08)
        
        # 退出按钮
        tk.Button(
            self.menu_frame, 
            text='退出系统', 
            command=self.root.quit,
            **btn_style
        ).place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.08)
        
    
    @audit_log(user_role="学生查询个人信息", action="show_student_info")
    
    def show_student_info(self):
        """显示学生个人信息"""
        # 清除现有内容
        if hasattr(self, 'content_frame'):
            self.content_frame.destroy()
            
        # 创建内容区域
        self.content_frame = tk.Frame(self.root)
        self.content_frame.place(relx=MENU_WIDTH_RATIO, relheight=1, relwidth=1-MENU_WIDTH_RATIO)
        
        # 标题
        tk.Label(
            self.content_frame, 
            text="个人信息", 
            font=('Microsoft YaHei', 16, 'bold')
        ).place(x=50, y=20)
        
        # 获取学生信息
        try:
            db = pymysql.connect(
                host='localhost', 
                user='root', 
                password='Yz200409012041Ab', 
                database='userdate1'
            )
            cursor = db.cursor()
            cursor.execute(
                "SELECT * FROM tb_student WHERE studentID=%s", 
                (self.student_id,)
            )
            student = cursor.fetchone()
            db.close()
            
            if not student:
                tk.Label(self.content_frame, text="未找到该学生信息").pack()
                return
                
            # 显示学生信息
            labels = ['学号', '姓名', '性别', '年龄', '密码']
            for i, (label, value) in enumerate(zip(labels, student)):
                # 标签
                tk.Label(
                    self.content_frame, 
                    text=f"{label}:", 
                    font=('Microsoft YaHei', 12),
                    width=8,
                    anchor='e'
                ).place(x=TEXT_INDENT, y=80+i*LINE_HEIGHT)
                
                # 值
                if label == '密码':
                    self.password_var = tk.StringVar(value=value)
                    tk.Entry(
                        self.content_frame, 
                        textvariable=self.password_var, 
                        font=('Microsoft YaHei', 12),
                        width=20
                    ).place(x=TEXT_INDENT+100, y=80+i*LINE_HEIGHT)
                else:
                    tk.Label(
                        self.content_frame, 
                        text=value, 
                        font=('Microsoft YaHei', 12),
                        width=20,
                        anchor='w'
                    ).place(x=TEXT_INDENT+100, y=80+i*LINE_HEIGHT)
           
        except Exception as e:
            messagebox.showerror("数据库错误", f"无法获取学生信息:\n{str(e)}")
    
    def show_student_grades(self):
        """显示学生课程成绩"""
        # 清除现有内容
        if hasattr(self, 'content_frame'):
            self.content_frame.destroy()
            
        # 创建内容区域
        self.content_frame = tk.Frame(self.root)
        self.content_frame.place(relx=MENU_WIDTH_RATIO, relheight=1, relwidth=1-MENU_WIDTH_RATIO)
        
        # 标题
        tk.Label(
            self.content_frame, 
            text="课程成绩", 
            font=('Microsoft YaHei', 16, 'bold')
        ).place(x=50, y=20)
        
        # 获取课程成绩
        try:
            db = pymysql.connect(
                host='localhost', 
                user='root', 
                password='Yz200409012041Ab', 
                database='userdate1'
            )
            cursor = db.cursor()
            
            # 查询学生课程成绩
            query = """
            SELECT 
                c.courseID, 
                c.courseName, 
                t.teacherName, 
                c.courseCredit,
                c.classTime,
                c.classroom,
                sc.grade
            FROM tb_student_course sc
            JOIN tb_course c ON sc.courseID = c.courseID AND sc.courseNum = c.courseNum
            JOIN tb_teacher_course tc ON c.courseID = tc.courseID AND c.courseNum = tc.courseNum
            JOIN tb_teacher t ON tc.teacherID = t.teacherID
            WHERE sc.studentID = %s
            ORDER BY c.courseID
            """
            cursor.execute(query, (self.student_id,))
            courses = cursor.fetchall()
            db.close()
            
            if not courses:
                tk.Label(
                    self.content_frame, 
                    text="该学生暂无课程成绩",
                    font=('Microsoft YaHei', 12)
                ).place(x=50, y=80)
                return
                
            # 创建表格显示课程成绩
            columns = ('课程编号', '课程名称', '授课教师', '学分', '上课时间', '上课地点', '成绩')
            tree = ttk.Treeview(
                self.content_frame, 
                columns=columns, 
                show='headings',
                height=15
            )
            
            # 设置列宽和标题
            col_widths = [80, 120, 80, 50, 120, 100, 50]
            for col, width in zip(columns, col_widths):
                tree.heading(col, text=col)
                tree.column(col, width=width, anchor='center')
            
            # 添加数据
            for course in courses:
                tree.insert('', 'end', values=course)
            
            # 添加滚动条
            scrollbar = ttk.Scrollbar(
                self.content_frame, 
                orient="vertical", 
                command=tree.yview
            )
            tree.configure(yscrollcommand=scrollbar.set)
            
            # 布局
            tree.place(x=20, y=60, width=860, height=500)
            scrollbar.place(x=880, y=60, height=500)
               
            # 添加统计信息
            valid_grades = [c[-1] for c in courses if c[-1] is not None and c[-1] >= 0]
            total_courses = len(courses)
            avg_grade = sum(valid_grades) / len(valid_grades) if valid_grades else 0
            total_credits = sum(c[3] for c in courses)
            max_grade = max(valid_grades) if valid_grades else 0  # 新增：计算最高分
            min_grade = min(valid_grades) if valid_grades else 0 
            stats_text = (f"总课程数: {total_courses} | "
             f"平均成绩: {avg_grade:.1f} | "
             f"最高分: {max_grade} | " 
             f"最低分: {min_grade} | "
             f"总学分: {total_credits}")
            tk.Label(
            self.content_frame,
            text=stats_text,
            font=('Microsoft YaHei', 12),
            fg='blue'
             ).place(x=20, y=570)
            
        except Exception as e:
            messagebox.showerror("数据库错误", f"无法获取课程成绩:\n{str(e)}")
    
           
if __name__ == '__main__':
    # 启动系统，显示学号为202301的学生信息
    app = menu('202301')
    app.root.mainloop()