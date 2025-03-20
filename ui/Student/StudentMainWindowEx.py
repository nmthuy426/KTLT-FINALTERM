from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow
from ui.Student.StudentMainWindow import Ui_MainWindow
from libs.JsonFileFactory import JsonFileFactory
import os

class StudentMainWindowExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.student_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/students.json"))
        self.jff = JsonFileFactory()
        self.SignalAndSlot()

        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def showWindow(self):
        self.MainWindow.show()

    def SignalAndSlot(self):
        self.pushButton_Exit.clicked.connect(self.process_exit)

    def process_exit(self):
        reply = QMessageBox.question(
            self.MainWindow,  # ✅ Đảm bảo hộp thoại thuộc về cửa sổ chính
            "Exit Confirmation",
            "Do you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            print("Exiting application...")
            self.MainWindow.close()

    def load_student_info(self, email):  # ✅ Đảm bảo thụt lề đúng
        try:
            students_data = self.jff.read_data(self.student_file, dict) or {}

            print(f"📌 [DEBUG] Kiểu dữ liệu students_data: {type(students_data)}")
            student_info = next(
                (s for s in students_data if
                 isinstance(s, dict) and s.get("email", "").strip().lower() == email.lower()), None)

            if not student_info:
                print("⚠️ Không tìm thấy sinh viên với email:", email)
                return

            self.lineEdit_StuId.setText(student_info.get("user_id", ""))
            self.lineEdit_StuFullname.setText(student_info.get("fullname", ""))
            birthday_str = student_info.get("birthday", "")
            if birthday_str:
                self.dateEdit_StuBir.setDate(QDate.fromString(birthday_str, "yyyy-MM-dd"))
            self.comboBox_StuGender.setCurrentText(student_info.get("gender", ""))
            self.lineEdit_StuMail.setText(student_info.get("email", ""))
            self.LineEdit_StuCourse.setText(student_info.get("course", ""))
            self.LineEdit_StuMajor.setText(student_info.get("major", ""))
            self.LineEdit_StuClass.setText(student_info.get("student_class", ""))
            self.LineEdit_StuAdvisor.setText(student_info.get("advisor", ""))

        except Exception as e:
            print("Lỗi khi load thông tin sinh viên:", e)

        print(f"📌 [DEBUG] Dữ liệu students_data từ JSON: {students_data}")