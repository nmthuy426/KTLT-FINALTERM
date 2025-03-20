from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import  QMessageBox, QTableWidgetItem,QCheckBox,QHeaderView,QTableWidget

from ui.Student.StudentMainWindow import Ui_MainWindow
import json
from libs.JsonFileFactory import JsonFileFactory
from models.Student import Student
from models.Class import Class
import os

class StudentMainWindowExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.class_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/classes.json"))
        self.student_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/students.json"))



    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.jff = JsonFileFactory()
        self.setupSignalAndSlot()

        self.show_classes_ui()

        # Kích hoạt hiệu ứng nền trong suốt
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        MainWindow.setStyleSheet("""
            background-color: rgba(0,32,96,150);
            border-radius: 10px;  /* Bo tròn góc cho đẹp hơn */
        """)

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_save.clicked.connect(self.save_selected_classes)

    def load_student_info(self, email):  # Tab Personal Information
        try:
            # Đọc danh sách sinh viên
            students_data = self.jff.read_data(self.student_file, Student) or []

            print(f"📌 [DEBUG] students_data sau khi đọc file: {students_data}")
            print(f"📌 [DEBUG] Kiểu của từng phần tử trong students_data: {[type(s) for s in students_data]}")
            # Kiểm tra kiểu dữ liệu
            print(f"📌 [DEBUG] Kiểu dữ liệu students_data: {type(students_data)}")
            if not isinstance(students_data, list):
                print("⚠️ Lỗi: students_data không phải list!")
                return

            # Tìm sinh viên theo email
            student_info = next((s for s in students_data if getattr(s, "email", "").strip().lower() == email.lower()),
                                None)

            if not student_info:
                print(f"⚠️ Không tìm thấy sinh viên với email: {email}")
                return

            print(f"✅ [DEBUG] Tìm thấy sinh viên: {student_info}")  # Kiểm tra xem có tìm được sinh viên không
            student_info = student_info.to_dict() if hasattr(student_info, "to_dict") else vars(student_info)
            print(f"📌 [DEBUG] Dữ liệu student_info (dict): {student_info}")  # In ra để chắc chắn nó là dict

            # Hiển thị thông tin lên giao diện (Dùng .get() thay vì getattr)
            self.lineEdit_StuId.setText(student_info.get("user_id", ""))
            self.lineEdit_StuFullname.setText(student_info.get("fullname", ""))

            birthday_str = student_info.get("birthday", "")
            if birthday_str:
                self.dateEdit_StuBir.setDate(QDate.fromString(birthday_str, "dd/MM/yyyy"))

            self.comboBox_StuGender.setCurrentText(student_info.get("gender", ""))
            self.lineEdit_StuMail.setText(student_info.get("email", ""))
            self.LineEdit_StuCourse.setText(student_info.get("course", ""))
            self.LineEdit_StuMajor.setText(student_info.get("major", ""))
            self.LineEdit_StuClass.setText(student_info.get("student_class", ""))
            self.LineEdit_StuAdvisor.setText(student_info.get("advisor", ""))

        except Exception as e:
            print("Lỗi khi load thông tin sinh viên:", e)

        print(f"📌 [DEBUG] Dữ liệu students_data từ JSON: {students_data}")

    def show_classes_ui(self):  # Tab Register
        """Đọc dữ liệu từ file JSON và hiển thị lên bảng"""
        classes_data = self.jff.read_data(self.class_file, Class) or []

        print(f"📌 [DEBUG] Kiểu dữ liệu classes_data: {type(classes_data)}")

        self.tableWidget_registeclass.setColumnCount(5)  # Khai báo số cột trước
        self.tableWidget_registeclass.setHorizontalHeaderLabels(
            ["Class ID", "Subject", "Room", "Schedule", "Select"])

        self.tableWidget_registeclass.setRowCount(len(classes_data))
        self.tableWidget_registeclass.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for row, item in enumerate(classes_data):
            self.tableWidget_registeclass.setItem(row, 0, QTableWidgetItem(getattr(item, "class_id", "")))
            self.tableWidget_registeclass.setItem(row, 1, QTableWidgetItem(getattr(item,"subject", "")))
            self.tableWidget_registeclass.setItem(row, 2, QTableWidgetItem(getattr(item,"room", "")))
            self.tableWidget_registeclass.setItem(row, 3, QTableWidgetItem(getattr(item, "schedule", "")))

            # Thêm checkbox vào cột cuối
            checkbox = QCheckBox()
            checkbox.setStyleSheet("margin-left:50%;")
            self.tableWidget_registeclass.setCellWidget(row, 4, checkbox)

        print("📌 [DEBUG] Đang chạy show_classes_ui()...")
        classes_data = self.jff.read_data(self.class_file, Class) or []

        print(f"📌 [DEBUG] Dữ liệu classes: {classes_data}")

    def save_selected_classes(self):
        """Lưu các lớp đã chọn trực tiếp vào students.json và classes.json"""
        student_email = self.lineEdit_StuMail.text().strip()  # Lấy email sinh viên từ giao diện
        if not student_email:
            print("❌ Không có email sinh viên!")
            return

        for row in range(self.tableWidget_registeclass.rowCount()):
            checkbox = self.tableWidget_registeclass.cellWidget(row, 4)
            if checkbox and checkbox.isChecked():  # Nếu checkbox được chọn
                class_id = self.tableWidget_registeclass.item(row, 0).text()

                # Gọi hàm `save_student_registration` để cập nhật vào students.json và classes.json
                self.save_student_registration(student_email, class_id)

        print("✅ Đã cập nhật danh sách lớp vào students.json và classes.json")

    def save_student_registration(self, student_email, class_id):
        'nhỏ này đ có chạy dc, có j nghía xuống cái note t để ở dưới thấy code dễ hiểu hơn'
        """Lưu đăng ký lớp học trực tiếp vào students.json và classes.json"""
        try:
            students_data = self.jff.read_data(self.student_file, Student) or []
            classes_data = self.jff.read_data(self.class_file, Class) or []

            # Chuyển students_data từ list[dict] → list[Student]
            if isinstance(students_data, list) and all(isinstance(s, dict) for s in students_data):
                students_data = [Student(**s) for s in students_data]

            # Chuyển classes_data từ list[dict] → list[Class]
            if isinstance(classes_data, list) and all(isinstance(c, dict) for c in classes_data):
                classes_data = [Class(**c) for c in classes_data]

            # Tìm sinh viên theo email
            student = next((s for s in students_data if s.email.strip().lower() == student_email.lower()), None)
            if not student:
                print("⚠️ Không tìm thấy sinh viên:", student_email)
                return False

            # Tìm lớp học theo class_id
            class_info = next((c for c in classes_data if c.class_id == class_id), None)
            if not class_info:
                print("⚠️ Không tìm thấy lớp:", class_id)
                return False

            # Nếu sinh viên chưa có danh sách lớp đăng ký thì tạo mới
            if not hasattr(student, "registered_classes") or not isinstance(student.registered_classes, list):
                student.registered_classes = []

            # Nếu lớp chưa được đăng ký thì thêm vào
            if class_id not in student.registered_classes:
                student.registered_classes.append(class_id)

            # Xử lý danh sách sinh viên của lớp
            if not hasattr(class_info, "students") or not isinstance(class_info.students, list):
                class_info.students = []

            # Nếu danh sách students là list chứa dict, chỉ lấy fullname
            elif all(isinstance(s, dict) for s in class_info.students):
                class_info.students = [s.get("fullname", "Unknown") for s in class_info.students]

            student_name = student.fullname
            if student_name not in class_info.students:
                class_info.students.append(student_name)

            # Kiểm tra data trước khi ghi file
            print(f"📌 [DEBUG] students_data trước khi lưu: {students_data}")
            print(f"📌 [DEBUG] classes_data trước khi lưu: {classes_data}")

            # Ghi lại dữ liệu vào file JSON
            self.jff.write_data(self.student_file, [s.to_dict() for s in students_data])
            self.jff.write_data(self.class_file, [c.to_dict() for c in classes_data])

            print(f"✅ Đã lưu đăng ký lớp {class_id} cho sinh viên {student_name}")
            QMessageBox.information(self.MainWindow, "Success", "Đăng kí học phần thành công!")

            return True

        except Exception as e:
            print(f"❌ Lỗi khi lưu đăng ký: {e}")
            return False