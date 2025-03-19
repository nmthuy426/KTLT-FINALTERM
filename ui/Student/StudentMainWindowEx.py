from PyQt6.QtCore import Qt
from ui.Student.StudentMainWindow import Ui_MainWindow
from PyQt6.QtGui import QPixmap, QPainterPath, QRegion
from PyQt6.QtCore import QRect


class StudentMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def showWindow(self):
        self.MainWindow.show()
