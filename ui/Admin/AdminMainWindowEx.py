from PyQt6.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem
from PyQt6.QtGui import QIntValidator
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
        self.teacher_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/teachers.json"))
        self.student_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/students.json"))

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.jff = JsonFileFactory()

        # Chỉ cho phép nhập số từ 2000 đến 2100 vào Course
        self.LineEdit_StuCourse.setValidator(QIntValidator(2000, 2100))


        BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Lấy thư mục hiện tại
        self.student_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/students.json"))
        self.teacher_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/teachers.json"))

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
        self.load_teachers()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_StuAddInfo.clicked.connect(self.process_add_student)
        self.pushButton_TeaAddInfo.clicked.connect(self.process_add_teacher)
        self.lineEdit_StuFullname.textChanged.connect(self.update_student_email)
        self.lineEdit_TeaFullname.textChanged.connect(self.update_teacher_email)
        self.LineEdit_StuClass.textChanged.connect(self.update_student_advisor)

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

    def update_student_advisor(self):
        student_class = self.LineEdit_StuClass.text().strip()
        print(f"📌 Nhập lớp: {student_class}")

        if not student_class:
            self.LineEdit_StuAdvisor.clear()
            print("🚫 Không có lớp, xóa Advisor!")
            return

        try:
            teachers_data = self.jff.read_data(self.teacher_file, dict) or []
            if not isinstance(teachers_data, list):  # Kiểm tra lại dữ liệu giảng viên
                print("❌ Dữ liệu giảng viên không hợp lệ!")
                return
        except Exception as e:
            print(f"❌ Lỗi khi đọc dữ liệu giảng viên: {e}")
            return

        matching_teachers = [
            teacher.get("fullname", "Không rõ") for teacher in teachers_data
            if teacher.get("teacher_class", "").strip() == student_class
        ]

        advisor_name = matching_teachers[0] if matching_teachers else ""
        print(f"📢 Advisor: {advisor_name}")

        self.LineEdit_StuAdvisor.setText(advisor_name)

        try:
            students_data = self.jff.read_data(self.student_file, dict) or []

            with open(self.student_file, "w", encoding="utf-8") as file:
                json.dump(students_data, file, indent=4, ensure_ascii=False)
            print("💾 Dữ liệu đã được ghi vào JSON!")
        except IOError as e:
            print(f"❌ Lỗi khi ghi file: {e}")
            QMessageBox.warning(self.MainWindow, "Error", f"Lỗi khi ghi file: {e}")
        except Exception as e:
            print(f"❌ Lỗi không xác định: {e}")
            QMessageBox.warning(self.MainWindow, "Error", f"Lỗi không xác định: {e}")

        print(f"Student file: {self.student_file}")
        print(f"Teacher file: {self.teacher_file}")


    def load_students(self):
        students = self.jff.read_data(self.student_file, Student) or []
        self.tableWidget_Student.setRowCount(len(students))
        self.tableWidget_Student.setColumnCount(9)
        self.tableWidget_Student.setHorizontalHeaderLabels(
            ["ID", "Name", "Birthday", "Gender", "Email", "Course", "Major", "Class", "Advisor"]
        )

        self.tableWidget_Student.setColumnWidth(2, 150)  # Birthday
        self.tableWidget_Student.setColumnWidth(3, 100)  # Gender
        self.tableWidget_Student.setColumnWidth(4, 250)  # Email (lớn hơn để tránh "...")
        self.tableWidget_Student.setColumnWidth(5, 100)  # Course
        self.tableWidget_Student.setColumnWidth(6, 220)  # Major
        self.tableWidget_Student.setColumnWidth(7, 120)  # Class
        self.tableWidget_Student.setColumnWidth(8, 200)  # Advisor

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

    def load_teachers(self):
        teachers = self.jff.read_data(self.teacher_file, Teacher) or []
        self.tableWidget_Teacher.setRowCount(len(teachers))
        self.tableWidget_Teacher.setColumnCount(7)
        self.tableWidget_Teacher.setHorizontalHeaderLabels(
            ["ID", "Name", "Birthday", "Gender", "Email", "Faculty", "Class"]
        )
        self.tableWidget_Teacher.setColumnWidth(1, 200)  # Điều chỉnh số 200 tùy ý
        self.tableWidget_Teacher.setColumnWidth(2, 150)  # Điều chỉnh số 200 tùy ý

        for row, teacher in enumerate(teachers):
            self.tableWidget_Teacher.setItem(row, 0, QTableWidgetItem(str(getattr(teacher, "user_id", ""))))
            self.tableWidget_Teacher.setItem(row, 1, QTableWidgetItem(str(getattr(teacher, "fullname", ""))))
            self.tableWidget_Teacher.setItem(row, 2, QTableWidgetItem(str(getattr(teacher, "birthday", ""))))
            self.tableWidget_Teacher.setItem(row, 3, QTableWidgetItem(str(getattr(teacher, "gender", ""))))
            self.tableWidget_Teacher.setItem(row, 4, QTableWidgetItem(str(getattr(teacher, "email", ""))))
            self.tableWidget_Teacher.setItem(row, 5, QTableWidgetItem(str(getattr(teacher, "faculty", ""))))
            self.tableWidget_Teacher.setItem(row, 6, QTableWidgetItem(str(getattr(teacher, "teacher_class", ""))))

    def validate_advisor(self, advisor_name):
        teachers = self.jff.read_data(self.teacher_file, Teacher) or []
        teacher_names = [teacher.fullname for teacher in teachers]
        return advisor_name in teacher_names

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

        if not self.validate_advisor(advisor):
            print("❌ Giáo viên không tồn tại!")
            QMessageBox.warning(self.MainWindow, "Error", "Giáo viên không tồn tại!")
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

    def process_add_teacher(self):
        print("🔍 Bắt đầu thêm giảng viên...")

        # Đọc dữ liệu từ file JSON
        teachers_data = self.jff.read_data(self.teacher_file, dict) or []
        print(f"📂 Đọc dữ liệu thành công! Số lượng giảng viên hiện có: {len(teachers_data)}")

        # Lấy dữ liệu từ giao diện
        teaid = self.lineEdit_TeaId.text().strip()
        name = self.lineEdit_TeaFullname.text().strip()
        birthday = self.dateEdit_TeaBir.text().strip()
        gender = self.comboBox_TeaGender.currentText().strip()
        email = self.lineEdit_TeaMail.text().strip()
        faculty = self.lineEdit_TeaFaculty.text().strip()
        cl = self.lineEdit_TeaClass.text().strip()

        print(f"📋 Dữ liệu nhập: {teaid}, {name}, {birthday}, {gender}, {email}, {faculty}, {cl}")

        if not all([teaid, name, birthday, gender, email, faculty, cl]):
            print("❌ Lỗi: Dữ liệu không đầy đủ!")
            QMessageBox.warning(self.MainWindow, "Error", "Vui lòng điền đầy đủ thông tin sinh viên!")
            return

        if any(teacher["user_id"] == teaid for teacher in teachers_data):
            print(f"⚠️ ID {teaid} đã tồn tại!")
            QMessageBox.warning(self.MainWindow, "Error", f"ID {teaid} đã tồn tại!")
            return

        new_teacher = {
            "user_id": teaid,
            "fullname": name,
            "birthday": birthday,
            "gender": gender,
            "email": email,
            "password": "12345",
            "faculty": faculty,
            "teacher_class": cl,
            "assigned_classes": []
        }

        print(f"✅ Thêm giảng viên: {new_teacher}")

        teachers_data.append(new_teacher)

        # 🛠 Ghi file JSON TRỰC TIẾP để kiểm tra lỗi
        try:
            with open(self.teacher_file, "w", encoding="utf-8") as file:
                json.dump(teachers_data, file, indent=4, ensure_ascii=False)
            print("💾 Dữ liệu đã được ghi vào JSON!")
        except Exception as e:
            print(f"❌ Lỗi khi ghi file JSON: {e}")
            QMessageBox.warning(self.MainWindow, "Error", f"Lỗi khi ghi file: {e}")
            return

        QMessageBox.information(self.MainWindow, "Success", "Teacher added successfully!")
        self.load_teachers()
