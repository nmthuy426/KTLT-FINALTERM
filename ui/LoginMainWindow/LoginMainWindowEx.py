from PyQt6.QtWidgets import QMessageBox, QMainWindow
from PyQt6.QtCore import pyqtSlot
from libs.DataConnector import DataConnector
from ui.Student.StudentMainWindow import Ui_MainWindow as StudentMainWindow  # Import UI Student
from ui.Teacher.TeacherMainWindow import Ui_MainWindow as TeacherMainWindow  # Import UI Teacher
from ui.LoginMainWindow.LoginMainWindow import Ui_MainWindow  # Import UI của màn hình đăng nhập


class LoginMainWindowEx(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Khởi tạo giao diện
        self.ui.setupUi(self)  # Gắn giao diện vào cửa sổ chính
        self.data_connector = DataConnector()  # Kết nối database

        # Kết nối nút đăng nhập với hàm xử lý
        self.ui.pushButton_Login.clicked.connect(self.process_login)

    @pyqtSlot()
    def process_login(self):
        """Xử lý đăng nhập"""
        email = self.ui.lineEdit_username.text().strip()
        password = self.ui.lineEdit_password.text().strip()

        print(f"📌 [DEBUG] Email nhập: {email}, Password nhập: {password}")  # Debug

        # Kiểm tra xem user có nhập dữ liệu không
        if not email or not password:
            print("⚠️ [DEBUG] Thiếu email hoặc password!")
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập Email và Mật khẩu!")
            return

        role, user_info = self.data_connector.login(email, password)  # Kiểm tra đăng nhập
        print(f"🔍 [DEBUG] Role nhận được: {role}, User Info: {user_info}")  # Debug dữ liệu từ DB

        if role in ["student", "teacher"]:
            QMessageBox.information(self, "Đăng nhập thành công",
                                    f"Xin chào {getattr(user_info, 'fullname', 'Người dùng')}!")

            self.open_user_interface(role, user_info)
        else:
            QMessageBox.warning(self, "Đăng nhập thất bại", "Sai Email hoặc Mật khẩu.")

    def open_user_interface(self, role, user):
        """Mở giao diện theo vai trò"""
        if role == "student":
            print(f"📌 Mở giao diện học sinh: {getattr(user, 'fullname', 'Không có tên')}")

            self.student_window = QMainWindow()  # Tạo cửa sổ mới
            self.student_ui = StudentMainWindow()
            self.student_ui.setupUi(self.student_window)
            self.student_window.show()
            self.student_window.activateWindow()  # Đảm bảo cửa sổ được kích hoạt

        elif role == "teacher":
            print(f"📌 Mở giao diện giáo viên: {getattr(user, 'fullname', 'Không có tên')}")
            self.teacher_window = QMainWindow()
            self.teacher_ui = TeacherMainWindow()
            self.teacher_ui.setupUi(self.teacher_window)
            self.teacher_window.show()
            self.teacher_window.activateWindow()

        self.close()  # Ẩn cửa sổ đăng nhập thay vì đóng luôn
