from PyQt6.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt6.QtCore import Qt
from libs.DataConnector import DataConnector
from ui.Student.StudentMainWindow import Ui_MainWindow as StudentMainWindow  # UI Student
from ui.Teacher.TeacherMainWindow import Ui_MainWindow as TeacherMainWindow  # UI Teacher
from ui.LoginMainWindow.LoginMainWindow import Ui_MainWindow

class LoginMainWindowExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = None
        self.student_window = None  # Giữ tham chiếu cửa sổ sinh viên
        self.teacher_window = None  # Giữ tham chiếu cửa sổ giáo viên
        self.data_connector = DataConnector()  # Kết nối database

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_Login.clicked.connect(self.process_login)
        self.pushButton_ForgetPassword.clicked.connect(self.forgetpassword)
        self.pushButton_Exit.clicked.connect(self.process_exit)

    def process_exit(self):
        print("Button clicked!")
        print("Type of self:", type(self))

        # Kiểm tra xem self có phải là QWidget hợp lệ không
        if not isinstance(self, QApplication):
            print("Warning: self is not a valid QWidget!")

        # Hiển thị hộp thoại xác nhận
        reply = QMessageBox.question(
            None,  # Đảm bảo self là một QWidget hợp lệ
            "Exit Confirmation",
            "Do you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        # Nếu chọn Yes thì thoát chương trình
        if reply == QMessageBox.StandardButton.Yes:
            print("Exiting application...")
            QApplication.quit()

    def forgetpassword(self):
        QMessageBox.information(self.MainWindow, "Quên mật khẩu", "Chức năng này đang được phát triển.")

    def process_login(self):
        """Xử lý đăng nhập"""
        email = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()

        print(f"📌 [DEBUG] Email nhập: {email}, Password nhập: {password}")  # Debug

        if not email or not password:
            print("⚠️ [DEBUG] Thiếu email hoặc password!")
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập Email và Mật khẩu!")
            return

        role, user_info = self.data_connector.login(email, password)  # Kiểm tra đăng nhập
        print(f"🔍 [DEBUG] Role nhận được: {role}, User Info: {user_info}")  # Debug

        if user_info is None:
            print("❌ [DEBUG] Không lấy được thông tin user!")
            QMessageBox.warning(self.MainWindow, "Lỗi", "Thông tin đăng nhập không hợp lệ!")
            return

        if role in ["student", "teacher"]:
            QMessageBox.information(self.MainWindow, "Đăng nhập thành công",
                                    f"Xin chào {getattr(user_info, 'fullname', 'Người dùng')}!")

            self.open_user_interface(role, user_info)
        else:
            QMessageBox.warning(self.MainWindow, "Đăng nhập thất bại", "Sai Email hoặc Mật khẩu.")

    def open_user_interface(self, role, user):
        """Mở giao diện theo vai trò"""
        fullname = getattr(user, 'fullname', 'Không có tên')
        print(f"📌 Mở giao diện {role}: {fullname}")

        if role == "student":
            if self.student_window is None:
                self.student_window = QMainWindow()
                self.student_ui = StudentMainWindow()
                self.student_ui.setupUi(self.student_window)
                self.student_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)

            self.student_window.show()
            self.student_window.activateWindow()

        elif role == "teacher":
            if self.teacher_window is None:
                self.teacher_window = QMainWindow()
                self.teacher_ui = TeacherMainWindow()
                self.teacher_ui.setupUi(self.teacher_window)

            self.teacher_window.show()
            self.teacher_window.activateWindow()

        self.MainWindow.close()  # Ẩn cửa sổ đăng nhập thay vì đóng hẳn