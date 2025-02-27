import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.LoginMainWindowEx import LoginMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Dùng sys.argv thay vì []

    login_window = QMainWindow()
    login_ui = LoginMainWindow()
    login_ui.setupUi(login_window)
    login_ui.showWindow()

    sys.exit(app.exec())  # Đảm bảo thoát đúng cách
