import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.Student.StudentMainWindowEx import StudentMainWindowExt

if __name__ == "__main__":
    app = QApplication(sys.argv)

    teacher_window = QMainWindow()
    teacher_ui = StudentMainWindowExt()
    teacher_ui.setupUi(teacher_window)
    teacher_ui.showWindow()

    sys.exit(app.exec())
