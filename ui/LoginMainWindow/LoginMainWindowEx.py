from PyQt6.QtCore import Qt
from ui.LoginMainWindow.LoginMainWindow import Ui_MainWindow

class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Kích hoạt hiệu ứng nền trong suốt
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        MainWindow.setStyleSheet("""
            background-color: rgba(0,46,255,100);
            border-radius: 10px;  /* Bo tròn góc cho đẹp hơn */
        """)

    def showWindow(self):
        self.MainWindow.show()
