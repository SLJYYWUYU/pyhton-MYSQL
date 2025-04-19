import functools
import datetime

def audit_log(user_role='未知角色', action='操作'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_id = '未知用户'
            try:
                self_obj = args[0]
                if hasattr(self_obj, 'student_id'):
                    user_id = self_obj.student_id
                elif hasattr(self_obj, 'managerNum'):
                    user_id = self_obj.managerNum
            except Exception:
                pass

            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_message = f"[{timestamp}] 用户 {user_id} 成功执行操作 [{user_role}]: {action}"

            try:
                result = func(*args, **kwargs)
                with open('audit_log.txt', 'a', encoding='utf-8') as f:
                    f.write(log_message + '\n')
                return result
            except Exception as e:
                error_msg = f"[{timestamp}] 用户 {user_id} 执行操作 [{user_role}] 出错: {action} 错误: {str(e)}"
                with open('audit_log.txt', 'a', encoding='utf-8') as f:
                    f.write(error_msg + '\n')
                raise
        return wrapper
    return decorator
