from PyQt6.QtWidgets import QMessageBox
from models.Student import Student
from libs.JsonFileFactory import JsonFileFactory


class AdminController:
    def __init__(self):
        self.jff = JsonFileFactory()
        self.students_file = "../dataset/students.json"

    def add_student(self, user_id, fullname, birthday, gender, password, student_class, major, course, advisor,
                    parent_window):
        students = self.jff.read_data(self.students_file, Student)

        for s in students:
            if s.user_id == user_id:
                # Hiển thị hộp thoại xác nhận cập nhật
                reply = QMessageBox.question(parent_window, "Xác nhận cập nhật",
                                             "ID này đã tồn tại - Bạn có muốn cập nhật lại thông tin cho học sinh này?",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                             QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    # Cập nhật thông tin sinh viên
                    s.fullname = fullname
                    s.birthday = birthday
                    s.gender = gender
                    s.password = password
                    s.student_class = student_class
                    s.major = major
                    s.course = course
                    s.advisor = advisor
                    self.jff.write_data(self.students_file, students)
                    return True  # Cập nhật thành công
                else:
                    return False  # Người dùng từ chối cập nhật

        # Nếu ID chưa tồn tại, thêm sinh viên mới
        student = Student(user_id, fullname, birthday, gender, password, student_class, major, course, advisor)
        students.append(student)
        self.jff.write_data(self.students_file, students)
        return True