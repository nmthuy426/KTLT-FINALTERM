from PyQt6.QtWidgets import QMessageBox, QMainWindow
from PyQt6.QtCore import Qt
from ui.LoginMainWindow import Ui_MainWindow

class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Kích hoạt hiệu ứng nền trong suốt
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Đặt màu nền RGBA(170,0,0,50)
        MainWindow.setStyleSheet("""
            background-color: rgba(170, 0, 0, 150);
            border-radius: 10px;  /* Bo tròn góc cho đẹp hơn */
        """)

    def showWindow(self):
        self.MainWindow.show()
