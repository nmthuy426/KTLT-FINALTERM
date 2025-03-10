from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from controllers.AdminControllers import AdminController
from ui.Admin.AdminMainWindow import Ui_AdminManagement


class AdminMainWindowExt(Ui_AdminManagement):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.admin_controller = AdminController()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_StuAddInfo.clicked.connect(self.add_student)

    def add_student(self):
        user_id = self.lineEdit_StuId.text()
        fullname = self.lineEdit_StuFullname.text()
        birthday = self.dateEdit_StuBir.text()
        gender = self.comboBox_StuGender.currentText()
        password = "123456"
        student_class = self.lineEdit_StuClass.text()
        major = self.lineEdit_StuMajor.text()
        course = self.lineEdit_StuCourse.text()
        advisor = self.lineEdit_advisor.text()

        # Lấy danh sách sinh viên từ file JSON
        students = self.admin_controller.get_students()

        # Kiểm tra ID đã tồn tại hay chưa
        existing_student = next((s for s in students if s['user_id'] == user_id), None)

        if existing_student:
            # Hiển thị hộp thoại xác nhận
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setWindowTitle("Cảnh báo")
            msg_box.setText(f"ID {user_id} đã tồn tại. Bạn có muốn cập nhật thông tin?")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            result = msg_box.exec()

            if result == QMessageBox.StandardButton.Yes:
                # Cập nhật thông tin sinh viên
                existing_student.update({
                    "fullname": fullname,
                    "birthday": birthday,
                    "gender": gender,
                    "student_class": student_class,
                    "major": major,
                    "course": course,
                    "advisor": advisor
                })
                self.admin_controller.update_students(students)
                QMessageBox.information(self.MainWindow, "Thành công", "Cập nhật thông tin sinh viên thành công!")
            else:
                QMessageBox.information(self.MainWindow, "Hủy bỏ", "Thông tin không thay đổi.")
        else:
            # Tạo đối tượng Student từ class OOP
            new_student = Student(user_id, fullname, birthday, gender, password, student_class, major, course, advisor)

            # Lấy email từ thuộc tính của Student (được sinh tự động)
            students.append({
                "user_id": new_student.user_id,
                "fullname": new_student.fullname,
                "birthday": new_student.birthday,
                "gender": new_student.gender,
                "password": new_student.password,
                "student_class": new_student.student_class,
                "major": new_student.major,
                "course": new_student.course,
                "advisor": new_student.advisor,
                "email": new_student.email  # Dùng email từ class Student
            })
            self.admin_controller.update_students(students)
            QMessageBox.information(self.MainWindow, "Thành công", "Thêm sinh viên thành công!")

        # Cập nhật bảng TableWidget
        self.update_student_table(students)

    def update_student_table(self, students):
        """ Hàm cập nhật dữ liệu vào QTableWidget """
        self.tableWidget_Student.setRowCount(len(students))
        for row, student in enumerate(students):
            self.tableWidget_Student.setItem(row, 0, QTableWidgetItem(student["user_id"]))
            self.tableWidget_Student.setItem(row, 1, QTableWidgetItem(student["fullname"]))
            self.tableWidget_Student.setItem(row, 2, QTableWidgetItem(student["student_class"]))
            self.tableWidget_Student.setItem(row, 3, QTableWidgetItem(student["email"]))  # Lấy email từ OOP
            self.tableWidget_Student.setItem(row, 4, QTableWidgetItem(student["password"]))
