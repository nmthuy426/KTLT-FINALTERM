from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.Admin.AdminMainWindowExt import AdminMainWindowExt
from ui.Student.StudentMainWindowEx import StudentMainWindowExt

app = QApplication([])

# Khởi tạo Student nhưng không mở cửa sổ ngay
student_window = QMainWindow()
student_ui = StudentMainWindowExt()
student_ui.setupUi(student_window)

# Khởi tạo Admin và truyền student_ui vào
admin_window = QMainWindow()
admin_ui = AdminMainWindowExt(student_ui)
admin_ui.setupUi(admin_window)

# Chỉ mở Admin trước, không mở Student
admin_window.show()

# Chạy app
app.exec()
