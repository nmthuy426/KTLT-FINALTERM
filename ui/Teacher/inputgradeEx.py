import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from libs.DataConnector import DataConnector
from libs.JsonFileFactory import JsonFileFactory
from ui.Teacher.inputgrade import Ui_MainWindow  # Import UI từ file .ui đã convert

class inputgradeExt(Ui_MainWindow):
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
        self.MainWindow.show()  # ✅ Sửa lỗi exec() -> show()

    def process_back(self):
        from ui.Teacher.TeacherMainWindowEx import TeacherMainWindowExt
        self.MainWindow.close()
        self.teacher_window = TeacherMainWindowExt(self)  # ✅ Tạo cửa sổ Admin đúng cách
        self.teacher_window.show()