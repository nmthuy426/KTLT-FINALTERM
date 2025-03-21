import json
import os
from PyQt6.QtWidgets import QMessageBox
from libs.DataConnector import DataConnector
from libs.JsonFileFactory import JsonFileFactory
from models.Teacher import Teacher
from ui.Admin.AdminMainWindowEx import AdminMainWindowExt
from ui.Admin.AdminMainWindow import Ui_AdminManagement  # ✅ Import class

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from ui.Admin.CreateClass import Ui_MainWindow

class CreateClassExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()  # Gọi constructor của QMainWindow
        self.setupUi(self)  # Gọi setup UI

        # Khởi tạo các biến cần thiết
        self.dc = DataConnector()
        self.students = []
        self.teachers = []
        self.jff = JsonFileFactory()
        self.teacher_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/teachers.json"))
        self.class_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/classes.json"))

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
        self.load_teacher_from_json()

    def setupSignalAndSlot(self):
        """Kết nối sự kiện của các nút bấm"""
        self.pushButton_SaveClass.clicked.connect(self.process_save_class)
        self.pushButton_Back.clicked.connect(self.process_back)
        self.lineEdit_Subject.textChanged.connect(self.capitalize_each_word_subject)
        self.lineEdit_ClassId.textChanged.connect(self.capitalize)

    def process_save_class(self):
        """Xử lý lưu lớp học vào file JSON và giữ cửa sổ mở"""
        class_id = self.lineEdit_ClassId.text().strip()
        subject = self.lineEdit_Subject.text().strip()
        teacher = self.comboBox.currentText().strip() or None
        schedule = self.lineEdit_Schedule.text().strip()
        room = self.lineEdit_Room.text().strip()
        major = self.lineEdit_Major.text().strip()
        min_students = 20
        max_students = 40

        if not (class_id and subject and schedule and room and major):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin bắt buộc!")
            return

        new_class = {
            "class_id": class_id,
            "teacher": teacher,
            "room": room,
            "schedule": schedule,
            "subject": subject,
            "major": major,
            "min_students": min_students,
            "max_students": max_students,
            "students": [],
            "grades": {}
        }

        file_path = self.class_file

        # Đọc dữ liệu hiện có
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    classes = json.load(file)
                    if not isinstance(classes, list):
                        classes = []
                except json.JSONDecodeError:
                    classes = []
        else:
            classes = []

        # Kiểm tra trùng ID lớp
        for existing_class in classes:
            if existing_class["class_id"] == class_id:
                QMessageBox.warning(self, "Lỗi", "Mã lớp đã tồn tại!")
                return

        # Thêm lớp mới vào danh sách
        classes.append(new_class)

        # Ghi dữ liệu vào file
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(classes, file, indent=4, ensure_ascii=False)

        QMessageBox.information(self, "Thành công", "Lớp học đã được lưu thành công!")
        self.clear()

    def capitalize_each_word_subject(self):
        text = self.lineEdit_Subject.text()
        capitalized = text.title()
        self.lineEdit_Subject.blockSignals(True)
        self.lineEdit_Subject.setText(capitalized)
        self.lineEdit_Subject.blockSignals(False)

    def capitalize(self):
        self.lineEdit_ClassId.setText(self.lineEdit_ClassId.text().upper())

    def clear(self):
        """✅ Xóa nội dung các ô nhập liệu để tiếp tục nhập lớp mới"""
        self.lineEdit_ClassId.clear()
        self.lineEdit_Subject.clear()
        self.comboBox.setCurrentIndex(0)  # Chọn lại mục đầu tiên
        self.lineEdit_Schedule.clear()
        self.lineEdit_Room.clear()
        self.lineEdit_Major.clear()

    def load_teacher_from_json(self):
        teachers = self.jff.read_data(self.teacher_file, Teacher) or []

        # Tạo dictionary lưu teacher_id theo fullname
        self.teacher_map = {teacher.fullname: teacher.teacher_id for teacher in teachers if teacher.fullname}

        # Hiển thị danh sách tên giáo viên trong comboBox
        self.comboBox.clear()
        self.comboBox.addItems(self.teacher_map.keys())

        print(f"📌 [DEBUG] Danh sách giáo viên: {self.teacher_map}")

    def process_back(self):
            self.close()
            admin_window = QMainWindow()  # Tạo QMainWindow trước
            admin_ui = AdminMainWindowExt(admin_window)  # Truyền vào class
            admin_ui.setupUi(admin_window)
            admin_ui.show()  # Hiển thị giao diện

