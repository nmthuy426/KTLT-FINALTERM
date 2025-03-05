import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.Teacher.TeacherMainWindowEx import TeacherMainWindowExt

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = QMainWindow()
    login_ui = TeacherMainWindowExt()
    login_ui.setupUi(login_window)

    login_ui.showWindow()

    sys.exit(app.exec())
