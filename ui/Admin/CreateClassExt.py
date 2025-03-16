import os

from libs.DataConnector import DataConnector
from libs.JsonFileFactory import JsonFileFactory
from ui.Admin.CreateClass import Ui_AddClassDialog


class CreateClassExt(Ui_AddClassDialog):
    def __init__(self, student_window):
        self.dc = DataConnector()
        self.students = []
        self.teachers = []
        self.student_window = student_window  # Giữ tham chiếu đến StudentMainWindow

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.jff = JsonFileFactory()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_SaveClass.clicked.connect(self.process_save_class)
        self.pushButton_Back.textChanged.connect(self.back_process)