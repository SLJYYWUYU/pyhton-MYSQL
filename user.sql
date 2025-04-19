USE  userdate1; 

CREATE TABLE IF NOT EXISTS tb_student(
    studentID char(6) NOT NULL COMMENT '学号',
    studentName varchar(10) NOT NULL DEFAULT '匿名' COMMENT '姓名',
    studentSex char(2) NOT NULL DEFAULT '男' COMMENT '性别',
    studentAge tinyint NOT NULL DEFAULT '18' COMMENT '年龄',
    studentPswd varchar(20) NOT NULL DEFAULT '123456' COMMENT '密码',
    PRIMARY KEY(studentID) 
)ENGINE=INNODB DEFAULT CHARSET=utf8 ;

CREATE TABLE IF NOT EXISTS tb_teacher(
    teacherID char(6) NOT NULL COMMENT '工号',
    teacherName varchar(10) NOT NULL DEFAULT '匿名' COMMENT '姓名',
    teacherSex char(2) NOT NULL DEFAULT '男' COMMENT '性别',
    teacherPswd varchar(20) NOT NULL DEFAULT '123456' COMMENT '密码',
    PRIMARY KEY (teacherID)
)ENGINE=INNODB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS tb_manager(
    managerID char(6)NOT NULL COMMENT '工号',
    managerName varchar(10)NOT NULL DEFAULT '匿名' COMMENT '姓名',
    managerPswd varchar(20) NOT NULL DEFAULT '123456' COMMENT '密码',
    PRIMARY KEY (managerID)
)ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS tb_course(
    courseID varchar(6) NOT NULL COMMENT '课程号',
    courseName varchar(20) NOT NULL DEFAULT '匿名' COMMENT '课程名',
    courseNum tinyint NOT NULL COMMENT '上课人数',
    courseCredit float NOT NULL DEFAULT 0 COMMENT '学分',
    courseHours SMALLINT NOT NULL DEFAULT 32 COMMENT '总学时数',
    classTime VARCHAR(50) NOT NULL COMMENT '上课时间',  
    classroom VARCHAR(30) NOT NULL COMMENT '上课地点',
    PRIMARY KEY (courseID, courseNum)
)ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS tb_teacher_course(
    teacherID char(6)NOT NULL COMMENT '工号',
    courseID char(6) NOT NULL COMMENT '课程号',
    courseNum tinyint NOT NULL COMMENT '上课人数',
    PRIMARY KEY (courseID, courseNum),
    FOREIGN KEY (teacherID) REFERENCES tb_teacher(teacherID),
    FOREIGN KEY (courseID, courseNum) REFERENCES tb_course(courseID, courseNum)
)ENGINE=INNODB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS tb_student_course(
    studentID char(6) NOT NULL COMMENT '学号',
    courseID char(6) NOT NULL COMMENT '课程号',
    courseNum tinyint NOT NULL COMMENT '上课人数',
    grade smallint NULL DEFAULT -1 COMMENT '成绩',
    PRIMARY KEY (studentID, courseID, courseNum),
    FOREIGN KEY (studentID) REFERENCES tb_student(studentID),
    FOREIGN KEY (courseID, courseNum) REFERENCES tb_course(courseID, courseNum)
)ENGINE=INNODB DEFAULT CHARSET=utf8;

insert into tb_student values('202301','李铭','男','18','123456');
insert into tb_student values('202302','刘晓鸣','男','19','123456');
insert into tb_student values('202303','李明','男','20','123456');
insert into tb_student values('202304','张鹰','女','19','123456');
insert into tb_student values('202305','刘竟静','女','18','123456');
insert into tb_student values('202306','刘成刚','男','19','123456');
insert into tb_student values('202307','王铭','男','20','123456');
insert into tb_student values('202308','宣明尼','女','18','123456');
insert into tb_student values('202309','柳红利','女','19','123456');


insert into tb_teacher values('20001', '陈蓉', '女', '123456');
insert into tb_teacher values('20002', '李晓华', '女', '123456'); 
insert into tb_teacher values('20003', '何军', '男', '123456');
insert into tb_teacher values('20004', '熊运余', '男', '123456');


insert into tb_manager values('200101', '李明', '123456');
insert into tb_manager values('200102', '王鹏', '123456');
insert into tb_manager values('200103', '大壮', '123456');

insert into tb_course values('A1-101', '程序开发基础', 5, 4,'56','周一1-2节','教学楼102');
insert into tb_course values('S1-103', '面向对象程序设计', 4, 4,'56','周三2-4节','教学楼201');
insert into tb_course values('A2-201', '数据结构与算法', 5, 4,'56','5周四3-4节','教学楼206');
insert into tb_course values('A2-202', '操作系统', 6, 4,'56','周五2-3节','教学楼305' );

insert into tb_teacher_course values('20001', 'A1-101', 5);
insert into tb_teacher_course values('20002', 'S1-103', 4);
insert into tb_teacher_course values('20003', 'A2-201', 5);
insert into tb_teacher_course values('20004', 'A2-202', 6);


insert into tb_student_course values('202301','A1-101', 5, 83);
insert into tb_student_course values('202302', 'A1-101', 5, 85);
insert into tb_student_course values('202303', 'A1-101', 5, 72);
insert into tb_student_course values('202304', 'A1-101', 5, 91);
insert into tb_student_course values('202305', 'A1-101', 5, 69);

insert into tb_student_course values('202304', 'S1-103', 4, 87);
insert into tb_student_course values('202305', 'S1-103', 4, 75);
insert into tb_student_course values('202306', 'S1-103', 4, 78);
insert into tb_student_course values('202307', 'S1-103', 4, 82);


insert into tb_student_course values('202301', 'A2-201', 5, 92);
insert into tb_student_course values('202302', 'A2-201', 5, 73);
insert into tb_student_course values('202303', 'A2-201', 5, 85);
insert into tb_student_course values('202308', 'A2-201', 5, 86);
insert into tb_student_course values('202309', 'A2-201', 5, 89);

insert into tb_student_course values('202301', 'A2-202', 6, 81);
insert into tb_student_course values('202302', 'A2-202', 6, 65);
insert into tb_student_course values('202306', 'A2-202', 6, 74);
insert into tb_student_course values('202307', 'A2-202', 6, 53);
insert into tb_student_course values('202308', 'A2-202', 6, 92);
insert into tb_student_course values('202309', 'A2-202', 6, 83);


-- 新增课程1
INSERT INTO tb_course 
VALUES('B1-301', '人工智能基础', 3, 3, 48, '周二1-3节', '教学楼401');


INSERT INTO tb_course 
VALUES('B2-305', '计算机网络', 2, 4, 56, '周四2-4节', '教学楼402');

-- 新增课程3
INSERT INTO tb_course 
VALUES('B3-308', 'Python数据分析', 2, 3, 48, '周三1-2节', '实验楼101');


INSERT INTO tb_course 
VALUES('B3-301', '语文', 2, 3, 48, '周三3-4节', '实验楼105');


INSERT INTO tb_course 
VALUES('B3-302', '数学', 2, 3, 48, '周五1-2节', '实验楼102');


INSERT INTO tb_course
VALUES('B3-303', '英语', 2, 3, 48, '周二1-2节', '实验楼103');


INSERT INTO tb_course 
VALUES('B3-304', '物理', 2, 3, 48, '周一1-2节', '实验楼104');


