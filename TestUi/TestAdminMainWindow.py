import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.Admin.AdminMainWindowEx import AdminMainWindowExt  # Đảm bảo đường dẫn đúng

if __name__ == "__main__":
    app = QApplication(sys.argv)

    admin_window = QMainWindow()  # Tạo QMainWindow trước
    admin_ui = AdminMainWindowExt(admin_window)  # Truyền vào class
    admin_ui.setupUi(admin_window)
    admin_ui.show()  # Hiển thị giao diện
    sys.exit(app.exec())
