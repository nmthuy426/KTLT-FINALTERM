from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui.Admin.ListOfStudents import Ui_MainWindow  # Import UI từ file .ui đã convert
import json  # Import thêm để đọc file JSON

class ListOfStudentsWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, class_id):
        super().__init__()
        self.setupUi(self)  # Load giao diện từ file .ui

        self.class_id = class_id  # Lưu class_id để dùng sau
        self.load_students()  # Tự động load danh sách sinh viên khi mở cửa sổ

        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButton_Home.clicked.connect(self.process_back)

    def showWindow(self):
        self.show()  # ✅ Sửa lỗi exec() -> show()

    def process_back(self):
        from ui.Admin.AdminMainWindowEx import AdminMainWindowExt
        self.close()
        self.admin_window = AdminMainWindowExt(self)  # ✅ Tạo cửa sổ Admin đúng cách
        self.admin_window.show()

    def load_students(self):
        """Load danh sách sinh viên của lớp vào tableWidget"""
        try:
            with open("dataset/students.json", "r", encoding="utf-8") as file:
                students = json.load(file)  # ✅ Đọc file JSON trực tiếp
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "File students.json not found!")
            return

        class_students = [s for s in students if s.get("student_class") == self.class_id]

        self.tableWidget_Students.setRowCount(len(class_students))
        self.tableWidget_Students.setColumnCount(5)
        self.tableWidget_Students.setHorizontalHeaderLabels(
            ["ID", "Full Name", "Birthday", "Email", "Gender"]
        )

        for row, student in enumerate(class_students):
            self.tableWidget_Students.setItem(row, 0, QTableWidgetItem(student.get("user_id", "")))
            self.tableWidget_Students.setItem(row, 1, QTableWidgetItem(student.get("fullname", "")))
            self.tableWidget_Students.setItem(row, 2, QTableWidgetItem(student.get("birthday", "")))
            self.tableWidget_Students.setItem(row, 3, QTableWidgetItem(student.get("email", "")))
            self.tableWidget_Students.setItem(row, 4, QTableWidgetItem(student.get("gender", "")))

        print(f"✅ Loaded {len(class_students)} students for class {self.class_id}")
