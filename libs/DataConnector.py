from models.Student import Student
from models.Teacher import Teacher
from models.Class import Class
from libs.JsonFileFactory import JsonFileFactory


class DataConnector:
    def get_all_students(self):
        jff = JsonFileFactory()
        filename = "../dataset/students.json"
        students = jff.read_data(filename, Student)
        return students

    def get_all_teachers(self):
        jff = JsonFileFactory()
        filename = "../dataset/teachers.json"
        teachers = jff.read_data(filename, Teacher)
        return teachers

    def get_all_classes(self):
        jff = JsonFileFactory()
        filename = "../dataset/classrooms.json"
        classrooms = jff.read_data(filename, Class)
        return classrooms

    def login(self, email, password):
        """Xác thực người dùng dựa trên email và mật khẩu"""
        email = email.strip().lower()
        password = password.strip()

        # Kiểm tra danh sách học sinh
        students = self.get_all_students()
        for student in students:
            if getattr(student, "email", "").strip().lower() == email:
                if getattr(student, "password", "").strip() == password:
                    print(f"✅ Đăng nhập thành công (Student): {email}")
                    return "student", student
                else:
                    print("❌ Sai mật khẩu!")
                    return None, None

        # Kiểm tra danh sách giáo viên
        teachers = self.get_all_teachers()
        for teacher in teachers:
            if getattr(teacher, "email", "").strip().lower() == email:
                if getattr(teacher, "password", "").strip() == password:
                    print(f"✅ Đăng nhập thành công (Teacher): {email}")
                    return "teacher", teacher
                else:
                    print("❌ Sai mật khẩu!")
                    return None, None

        print("❌ Đăng nhập thất bại: Sai email hoặc mật khẩu!")
        return None, None

    def check_existing_student(self, students, stuid):
        print(f"🧐 Đang kiểm tra ID {stuid} trong danh sách...")

        for i, student in enumerate(students):
            print(f"👀 Kiểm tra {getattr(student, 'user_id', 'UNKNOWN')} với {stuid}...")

            if getattr(student, "user_id", None) == stuid:
                print(f"✅ Tìm thấy tại index {i}")
                return i

        print("❌ Không tìm thấy!")
        return -1

    def check_existing_teacher(self, teachers, teaid):
        for i, teacher in enumerate(teachers):
            if getattr(teacher, "user_id", None) == teaid:
                return i
        return -1