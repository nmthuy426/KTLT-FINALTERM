from PyQt6.QtCore import Qt
from ui.Student.StudentMainWindow import Ui_MainWindow

class StudentMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Kích hoạt hiệu ứng nền trong suốt
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        MainWindow.setStyleSheet("""
            background-color: rgba(0,32,96,150);
            border-radius: 10px;  /* Bo tròn góc cho đẹp hơn */
        """)

    def showWindow(self):
        self.MainWindow.show()
