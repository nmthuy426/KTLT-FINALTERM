import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from libs.DataConnector import DataConnector
from libs.JsonFileFactory import JsonFileFactory
from ui.Admin.ListOfStudents import Ui_MainWindow  # Import UI từ file .ui đã convert
import json  # Import thêm để đọc file JSON

class ListOfStudentsWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, class_id, student_list):
        super().__init__()
        self.setupUi(self)  # Load giao diện từ file .ui
        self.class_id = class_id
        self.student_list = student_list  # 🔥 Lưu danh sách sinh viên
        self.load_students()  # 🔥 Load danh sách sinh viên từ `student_list`

    def setupUi(self, MainWindow):
        """Thiết lập giao diện chính cho cửa sổ CreateClass"""
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setupSignalAndSlot()
        self.teacher_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/teachers.json"))
        self.class_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/classes.json"))
        self.dc = DataConnector()
        self.jff = JsonFileFactory()

    def setupSignalAndSlot(self):
        self.pushButton_back.clicked.connect(self.process_back)

    def showWindow(self):
        self.show()  # ✅ Sửa lỗi exec() -> show()

    def process_back(self):
        from ui.Admin.AdminMainWindowEx import AdminMainWindowExt
        self.close()
        self.admin_window = AdminMainWindowExt(self)  # ✅ Tạo cửa sổ Admin đúng cách
        self.admin_window.show()

    def load_students(self):
        """Hiển thị danh sách sinh viên của lớp lên bảng"""
        if not self.student_list:
            QMessageBox.warning(self, "Danh Sách Trống", f"Lớp {self.class_id} chưa có sinh viên đăng ký.")
            return

        self.tableWidget.setRowCount(len(self.student_list))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Full Name", "Birthday", "Email", "Gender", "Major"])

        self.tableWidget.setColumnWidth(1, 200)  # Subject
        self.tableWidget.setColumnWidth(2, 100)  # Room
        self.tableWidget.setColumnWidth(3, 300)  # Schedule
        self.tableWidget.setColumnWidth(4, 100)  # Teacher ID
        self.tableWidget.setColumnWidth(5, 200)

        for row, student in enumerate(self.student_list):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(student.get("user_id", "")))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(student.get("fullname", "")))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(student.get("birthday", "")))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(student.get("email", "")))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(student.get("gender", "")))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(student.get("major", "")))

        print(f"✅ Loaded {len(self.student_list)} students for class {self.class_id}")
