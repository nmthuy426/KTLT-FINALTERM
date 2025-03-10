from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QMainWindow

from libs.DataConnector import DataConnector
from ui.LoginMainWindow.LoginMainWindow import Ui_MainWindow
from ui.Student.StudentMainWindowEx import StudentMainWindowExt
from ui.Teacher.TeacherMainWindowEx import TeacherMainWindowExt


class LoginMainWindowExt(Ui_MainWindow):
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

    def setupSignalAndSlot(self):
        self.pushButton_Login.clicked.connect(self.process_login)

    def process_login(self):
        dc=DataConnector()
        email = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        user = dc.login(email, password)

        if not email or not password:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập Email và Mật khẩu.")
            return

        if user != None:
            self.MainWindow.close()  # Đóng cửa sổ login

            if user.role == "student":
                self.main_window = QMainWindow()
                self.main_ui = StudentMainWindowExt()
                self.main_ui.setupUi(self.main_window)
                self.main_ui.showWindow()

            elif user.role == "teacher":
                self.main_window = QMainWindow()
                self.main_ui = TeacherMainWindowExt()
                self.main_ui.setupUi(self.main_window)
                self.main_ui.showWindow()
        else:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Đăng nhập thất bại")
            self.msg.exec()
