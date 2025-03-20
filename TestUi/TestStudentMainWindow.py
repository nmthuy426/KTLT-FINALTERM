import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.Student.StudentMainWindowEx import StudentMainWindowExt

if __name__ == "__main__":
    app = QApplication(sys.argv)

    student_window = QMainWindow()
    student_ui = StudentMainWindowExt()
    student_ui.setupUi(student_window)
    student_ui.showWindow()

    sys.exit(app.exec())


