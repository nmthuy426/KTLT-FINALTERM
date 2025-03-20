from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt
from ui.Teacher.TeacherMainWindow import Ui_MainWindow
import json
import os


class TeacherMainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = None
        self.class_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/classes.json"))
        self.teacher_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/teachers.json"))

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        print("📌 [DEBUG] setupUi() đã chạy!")
        self.load_teacher_classes()  # Đảm bảo hàm này được gọi

    def load_teacher_classes(self):
        """Tải danh sách lớp mà giáo viên giảng dạy và hiển thị lên bảng."""
        print("📌 [DEBUG] Hàm load_teacher_classes() đã được gọi!")  # Debug
        try:
            file_path = self.class_file
            print(f"📌 [DEBUG] Đang đọc file {file_path}")

            with open(file_path, "r", encoding="utf-8") as f:
                classes_data = json.load(f) or []

            print(f"📌 [DEBUG] Dữ liệu lớp học: {classes_data}")  # Debug dữ liệu JSON

            if not classes_data:
                print("⚠️ [WARNING] Không có dữ liệu lớp học!")
                return

            # Cấu hình bảng hiển thị dữ liệu
            self.tableWidget_classes.setColumnCount(4)
            self.tableWidget_classes.setHorizontalHeaderLabels(
                ["Class ID", "Subject", "Room", "Schedule", "Select"]
            )
            self.tableWidget_classes.setRowCount(len(classes_data))
            self.tableWidget_classes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

            # Duyệt danh sách lớp học để hiển thị lên bảng
            for row, item in enumerate(classes_data):
                self.tableWidget_classes.setItem(row, 0, QTableWidgetItem(item.get("class_id", "")))
                self.tableWidget_classes.setItem(row, 1, QTableWidgetItem(item.get("subject", "")))
                self.tableWidget_classes.setItem(row, 2, QTableWidgetItem(item.get("room", "")))
                self.tableWidget_classes.setItem(row, 3, QTableWidgetItem(item.get("schedule", "")))

        except FileNotFoundError:
            print(f"❌ [ERROR] Không tìm thấy file {file_path}!")
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Không tìm thấy file {file_path}!")

        except json.JSONDecodeError as e:
            print(f"❌ [ERROR] Lỗi đọc JSON: {e}")
            QMessageBox.warning(self.MainWindow, "Lỗi", f"File JSON bị lỗi: {e}")
