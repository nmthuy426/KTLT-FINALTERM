import email
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.Teacher.TeacherMainWindowEx import TeacherMainWindowExt

if __name__ == "__main__":
    app = QApplication(sys.argv)

    teacher_window = QMainWindow()
    teacher_ui = TeacherMainWindowExt()
    teacher_ui.setupUi(teacher_window)
    teacher_ui.showWindow()

    sys.exit(app.exec())
