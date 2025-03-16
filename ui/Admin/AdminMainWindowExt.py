from PyQt6.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem
from ui.Admin.AdminMainWindow import Ui_AdminManagement
from models.Student import Student
from models.Teacher import Teacher
from libs.JsonFileFactory import JsonFileFactory
from libs.DataConnector import DataConnector
from models.User import User
import os
import json


class AdminMainWindowExt(Ui_AdminManagement):
    def __init__(self, student_window):
        self.dc = DataConnector()
        self.students = []
        self.teachers = []
        self.student_window = student_window  # Giữ tham chiếu đến StudentMainWindow

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.jff = JsonFileFactory()

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Lấy thư mục hiện tại
        self.student_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/students.json"))

        # Tạo thư mục dataset nếu chưa có
        dataset_folder = os.path.dirname(self.student_file)
        if not os.path.exists(dataset_folder):
            os.makedirs(dataset_folder)
            print(f"📂 Tạo thư mục: {dataset_folder}")

        # Nếu file students.json chưa tồn tại, tạo file rỗng
        if not os.path.exists(self.student_file):
            with open(self.student_file, "w", encoding="utf-8") as file:
                file.write("[]")  # Mảng trống để tránh lỗi khi đọc
            print(f"📄 Tạo file: {self.student_file}")

        # Load dữ liệu khi mở app
        self.load_students()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_StuAddInfo.clicked.connect(self.process_add_student)
        self.lineEdit_StuFullname.textChanged.connect(self.update_student_email)

    def load_students(self):
        students = self.jff.read_data(self.student_file, Student) or []
        self.tableWidget_Student.setRowCount(len(students))
        self.tableWidget_Student.setColumnCount(9)
        self.tableWidget_Student.setHorizontalHeaderLabels(
            ["ID", "Name", "Birthday", "Gender", "Email", "Course", "Major", "Class", "Advisor"]
        )

        for row, student in enumerate(students):
            self.tableWidget_Student.setItem(row, 0, QTableWidgetItem(str(getattr(student, "user_id", ""))))
            self.tableWidget_Student.setItem(row, 1, QTableWidgetItem(str(getattr(student, "fullname", ""))))
            self.tableWidget_Student.setItem(row, 2, QTableWidgetItem(str(getattr(student, "birthday", ""))))
            self.tableWidget_Student.setItem(row, 3, QTableWidgetItem(str(getattr(student, "gender", ""))))
            self.tableWidget_Student.setItem(row, 4, QTableWidgetItem(str(getattr(student, "email", ""))))
            self.tableWidget_Student.setItem(row, 5, QTableWidgetItem(str(getattr(student, "course", ""))))
            self.tableWidget_Student.setItem(row, 6, QTableWidgetItem(str(getattr(student, "major", ""))))
            self.tableWidget_Student.setItem(row, 7, QTableWidgetItem(str(getattr(student, "student_class", ""))))
            self.tableWidget_Student.setItem(row, 8, QTableWidgetItem(str(getattr(student, "advisor", ""))))

    def process_add_student(self):
        print("🔍 Bắt đầu thêm sinh viên...")

        # Đọc dữ liệu từ file JSON
        students_data = self.jff.read_data(self.student_file, dict) or []
        print(f"📂 Đọc dữ liệu thành công! Số lượng sinh viên hiện có: {len(students_data)}")

        # Lấy dữ liệu từ giao diện
        stuid = self.lineEdit_StuId.text().strip()
        name = self.lineEdit_StuFullname.text().strip()
        birthday = self.dateEdit_StuBir.text().strip()
        gender = self.comboBox_StuGender.currentText().strip()
        email = self.lineEdit_StuMail.text().strip()
        course = self.LineEdit_StuCourse.text().strip()
        major = self.LineEdit_StuMajor.text().strip()
        cl = self.LineEdit_StuClass.text().strip()
        advisor = self.LineEdit_StuAdvisor.text().strip()

        print(f"📋 Dữ liệu nhập: {stuid}, {name}, {birthday}, {gender}, {email}, {course}, {major}, {cl}, {advisor}")

        if not all([stuid, name, birthday, gender, email, course, major, cl, advisor]):
            print("❌ Lỗi: Dữ liệu không đầy đủ!")
            QMessageBox.warning(self.MainWindow, "Error", "Vui lòng điền đầy đủ thông tin sinh viên!")
            return

        if any(student["user_id"] == stuid for student in students_data):
            print(f"⚠️ ID {stuid} đã tồn tại!")
            QMessageBox.warning(self.MainWindow, "Error", f"ID {stuid} đã tồn tại!")
            return

        new_student = {
            "user_id": stuid,
            "fullname": name,
            "birthday": birthday,
            "gender": gender,
            "email": email,
            "password": "12345",
            "student_class": cl,
            "major": major,
            "course": course,
            "advisor": advisor,
            "registered_classes": [],
            "grades": {}
        }

        print(f"✅ Thêm sinh viên: {new_student}")

        students_data.append(new_student)

        # 🛠 Ghi file JSON TRỰC TIẾP để kiểm tra lỗi
        try:
            with open(self.student_file, "w", encoding="utf-8") as file:
                json.dump(students_data, file, indent=4, ensure_ascii=False)
            print("💾 Dữ liệu đã được ghi vào JSON!")
        except Exception as e:
            print(f"❌ Lỗi khi ghi file JSON: {e}")
            QMessageBox.warning(self.MainWindow, "Error", f"Lỗi khi ghi file: {e}")
            return

        QMessageBox.information(self.MainWindow, "Success", "Student added successfully!")
        self.load_students()

        if self.student_window:
            self.student_window.load_student_info_to_ui(new_student)

    def update_student_email(self):
        fullname = self.lineEdit_StuFullname.text()
        if fullname:
            email = User.generate_email(fullname, "student")
            self.lineEdit_StuMail.setText(email)

    def update_teacher_email(self):
        fullname = self.lineEdit_TeaFullname.text()
        if fullname:
            email = User.generate_email(fullname, "teacher")
            self.lineEdit_TeaMail.setText(email)
