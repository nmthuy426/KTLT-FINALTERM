from models.Student import Student
from models.Teacher import Teacher
from models.Class import Class
from libs.JsonFileFactory import JsonFileFactory

import os
import json

class DataConnector:
    def __init__(self):
        self.teachers_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/teachers.json"))
        self.classes_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/classes.json"))
        self.students_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/students.json"))
        self.grades_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/grades.json"))

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

    def get_current_user(self):
        """Lấy thông tin giáo viên hiện tại (giả lập)"""
        return {"teacher_id": "T001", "name": "Nguyễn Văn A"}  # Giả lập dữ liệu, thay bằng dữ liệu thực

    def get_classes_by_teacher(self, teacher_id):
        """Lấy danh sách lớp của giáo viên dựa trên ID"""
        try:
            with open(self.classes_file, "r", encoding="utf-8") as file:
                classes = json.load(file)
            return [cls for cls in classes if cls["teacher_id"] == teacher_id]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_students_by_class(self, class_id):
        """Lấy danh sách học sinh trong lớp dựa trên ID"""
        try:
            with open(self.students_file, "r", encoding="utf-8") as file:
                students = json.load(file)
            return [student for student in students if student["class_id"] == class_id]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_grades(self, class_id, grades):
        """Lưu điểm vào file JSON"""
        try:
            if os.path.exists(self.grades_file):
                with open(self.grades_file, "r", encoding="utf-8") as file:
                    all_grades = json.load(file)
            else:
                all_grades = {}

            all_grades[class_id] = grades  # Lưu điểm theo lớp

            with open(self.grades_file, "w", encoding="utf-8") as file:
                json.dump(all_grades, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Lỗi khi lưu điểm: {e}")

    def get_students_by_registered_class(self,class_id):
        """Lấy danh sách học sinh đã đăng ký vào một lớp cụ thể"""
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        class_file = os.path.join(base_dir, "dataset", "classes.json")
        student_file = os.path.join(base_dir, "dataset", "students.json")

        if not os.path.exists(class_file) or not os.path.exists(student_file):
            print("⚠ Lỗi: Không tìm thấy file dữ liệu!")
            return []

        try:
            # Đọc danh sách lớp
            with open(class_file, "r", encoding="utf-8") as file:
                classes_data = json.load(file)

            # Tìm lớp có `class_id`
            class_info = next((c for c in classes_data if c["class_id"] == class_id), None)
            if not class_info:
                print(f"⚠ Lỗi: Không tìm thấy lớp {class_id}!")
                return []

            student_ids = class_info.get("students", [])  # Danh sách `user_id` học sinh

            # Đọc danh sách học sinh
            with open(student_file, "r", encoding="utf-8") as file:
                students_data = json.load(file)

            # Lọc học sinh có trong danh sách `student_ids`
            enrolled_students = [s for s in students_data if s["user_id"] in student_ids]

            print(f"✅ {len(enrolled_students)} học sinh được tìm thấy trong lớp {class_id}")
            return enrolled_students

        except Exception as e:
            print(f"❌ Lỗi khi đọc dữ liệu: {e}")
            return []
