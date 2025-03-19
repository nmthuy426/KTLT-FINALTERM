from PyQt6.QtCore import Qt
from ui.Teacher.TeacherMainWindow import Ui_MainWindow

class TeacherMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)


    def showWindow(self):
        self.MainWindow.show()
