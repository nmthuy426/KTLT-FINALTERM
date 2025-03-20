from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import  QMessageBox, QTableWidgetItem,QCheckBox,QHeaderView,QTableWidget

from ui.Student.StudentMainWindow import Ui_MainWindow
from libs.JsonFileFactory import JsonFileFactory
from models.Student import Student
from models.Class import Class
import os
import json

class StudentMainWindowExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.class_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/classes.json"))
        self.student_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/students.json"))

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.jff = JsonFileFactory()
        self.setupSignalAndSlot()

        self.show_classes_to_stu_ui()

        self.class_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/classes.json"))
        self.student_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/students.json"))

        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_save.clicked.connect(self.save_selected_classes)
        self.pushButton_Exit.clicked.connect(self.process_exit)

    def load_student_info(self, email):  # Tab Personal Information
        try:
            # Đọc danh sách sinh viên
            students_data = self.jff.read_data(self.student_file, Student) or []

            print(f"📌 [DEBUG] students_data sau khi đọc file: {students_data}")
            print(f"📌 [DEBUG] Kiểu của từng phần tử trong students_data: {[type(s) for s in students_data]}")
            # Kiểm tra kiểu dữ liệu
            print(f"📌 [DEBUG] Kiểu dữ liệu students_data: {type(students_data)}")
            if not isinstance(students_data, list):
                print("⚠️ Lỗi: students_data không phải list!")
                return

            # Tìm sinh viên theo email
            student_info = next((s for s in students_data if getattr(s, "email", "").strip().lower() == email.lower()),
                                None)

            if not student_info:
                print(f"⚠️ Không tìm thấy sinh viên với email: {email}")
                return

            print(f"✅ [DEBUG] Tìm thấy sinh viên: {student_info}")  # Kiểm tra xem có tìm được sinh viên không
            student_info = student_info.to_dict() if hasattr(student_info, "to_dict") else vars(student_info)
            print(f"📌 [DEBUG] Dữ liệu student_info (dict): {student_info}")  # In ra để chắc chắn nó là dict

            # Hiển thị thông tin lên giao diện (Dùng .get() thay vì getattr)
            self.lineEdit_StuId.setText(student_info.get("user_id", ""))
            self.lineEdit_StuFullname.setText(student_info.get("fullname", ""))

            birthday_str = student_info.get("birthday", "")
            if birthday_str:
                self.dateEdit_StuBir.setDate(QDate.fromString(birthday_str, "dd/MM/yyyy"))

            self.comboBox_StuGender.setCurrentText(student_info.get("gender", ""))
            self.lineEdit_StuMail.setText(student_info.get("email", ""))
            self.LineEdit_StuCourse.setText(student_info.get("course", ""))
            self.LineEdit_StuMajor.setText(student_info.get("major", ""))
            self.LineEdit_StuClass.setText(student_info.get("student_class", ""))
            self.LineEdit_StuAdvisor.setText(student_info.get("advisor", ""))

        except Exception as e:
            print("Lỗi khi load thông tin sinh viên:", e)

        print(f"📌 [DEBUG] Dữ liệu students_data từ JSON: {students_data}")

    def show_classes_to_stu_ui(self):  # Tab Register
        """Đọc dữ liệu từ file JSON và hiển thị lên bảng"""
        classes_data = self.jff.read_data(self.class_file, Class) or []

        print(f"📌 [DEBUG] Kiểu dữ liệu classes_data: {type(classes_data)}")

        self.tableWidget_registeclass.setColumnCount(5)  # Khai báo số cột trước
        self.tableWidget_registeclass.setHorizontalHeaderLabels(
            ["Class ID", "Subject", "Room", "Schedule", "Select"])

        self.tableWidget_registeclass.setRowCount(len(classes_data))
        self.tableWidget_registeclass.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for row, item in enumerate(classes_data):
            self.tableWidget_registeclass.setItem(row, 0, QTableWidgetItem(getattr(item, "class_id", "")))
            self.tableWidget_registeclass.setItem(row, 1, QTableWidgetItem(getattr(item,"subject", "")))
            self.tableWidget_registeclass.setItem(row, 2, QTableWidgetItem(getattr(item,"room", "")))
            self.tableWidget_registeclass.setItem(row, 3, QTableWidgetItem(getattr(item, "schedule", "")))

            # Thêm checkbox vào cột cuối
            checkbox = QCheckBox()
            checkbox.setStyleSheet("margin-left:50%;")
            self.tableWidget_registeclass.setCellWidget(row, 4, checkbox)

        print("📌 [DEBUG] Đang chạy show_classes_ui()...")
        classes_data = self.jff.read_data(self.class_file, Class) or []

        print(f"📌 [DEBUG] Dữ liệu classes: {classes_data}")

    def save_selected_classes(self):
        student_email = self.lineEdit_StuMail.text().strip()
        if not student_email:
            print("❌ Không có email sinh viên!")
            return

        selected_classes = []
        for row in range(self.tableWidget_registeclass.rowCount()):
            checkbox = self.tableWidget_registeclass.cellWidget(row, 4)
            if checkbox and checkbox.isChecked():
                class_id = self.tableWidget_registeclass.item(row, 0).text()
                selected_classes.append(class_id)

        if not selected_classes:
            print("⚠️ Không có lớp nào được chọn!")
            return

        # 🔥 Đọc dữ liệu sinh viên từ JSON
        students_data = self.read_json_file(self.student_file)
        classes_data = self.read_json_file(self.class_file)


        # 🔥 Tìm sinh viên theo email
        student = next((s for s in students_data if s.get("email", "").strip().lower() == student_email.lower()), None)
        if not student:
            print(f"⚠️ Không tìm thấy sinh viên: {student_email}")
            return

        # 🔥 Ghi đè danh sách lớp: Xóa hết lớp cũ, chỉ lưu lớp mới
        student["registered_classes"] = selected_classes

        # 🔥 Cập nhật danh sách sinh viên trong từng lớp
        for class_obj in classes_data:
            if class_obj["class_id"] in selected_classes:
                if student["user_id"] not in class_obj["students"]:  # Tránh trùng lặp
                    class_obj["students"].append(student["user_id"])
            else:
                if student["user_id"] in class_obj["students"]:  # Xóa nếu lớp không còn được chọn
                    class_obj["students"].remove(student["user_id"])

        # 🔥 Ghi lại dữ liệu vào files
        self.write_data(self.student_file, students_data)
        self.write_data(self.class_file, classes_data)

        print(f"✅ Đã cập nhật danh sách lớp cho sinh viên {student_email}")
        QMessageBox.information(self.MainWindow, "Thành công", "Danh sách lớp của bạn đã được cập nhật!")

    def write_data(self, file_path, arr_data):
        """ Ghi dữ liệu vào JSON một cách an toàn """
        try:
            if not isinstance(arr_data, list):
                raise ValueError("❌ Dữ liệu đầu vào phải là danh sách!")

            # 🔥 Chuyển tất cả object thành dict nếu cần
            data_to_write = [obj.__dict__ if hasattr(obj, "__dict__") else obj for obj in arr_data]

            # 🔥 Ghi file an toàn
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data_to_write, file, indent=4, ensure_ascii=False)

        except Exception as e:
            print(f"❌ Lỗi khi ghi file {file_path}: {e}")

    def read_json_file(self, file_path):
        """ Đọc file JSON một cách an toàn """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    print("❌ Lỗi: Dữ liệu JSON không đúng format!")
                    return []
        except FileNotFoundError:
            print(f"⚠️ File {file_path} không tồn tại, sẽ tạo mới!")
            return []
        except json.JSONDecodeError:
            print(f"❌ Lỗi: File {file_path} bị hỏng, không thể đọc JSON!")
            return []
        except Exception as e:
            print(f"❌ Lỗi khi đọc file {file_path}: {e}")
            return []

    def load_registered_classes(self, student_email):
        """ Tự động check checkbox các lớp đã đăng ký khi đăng nhập """
        students_data = self.read_json_file(self.student_file)

        # 🔥 Tìm sinh viên theo email
        student = next((s for s in students_data if s.get("email", "").strip().lower() == student_email.lower()), None)
        if not student:
            print(f"⚠️ Không tìm thấy sinh viên: {student_email}")
            return

        registered_classes = set(student.get("registered_classes", []))  # Chuyển về set để so sánh nhanh

        # 🔥 Duyệt qua bảng và check checkbox nếu lớp đã đăng ký
        for row in range(self.tableWidget_registeclass.rowCount()):
            class_id = self.tableWidget_registeclass.item(row, 0).text()  # Lấy ID lớp
            checkbox = self.tableWidget_registeclass.cellWidget(row, 4)  # Lấy checkbox

            if checkbox:
                checkbox.setChecked(class_id in registered_classes)  # Check nếu lớp đã đăng ký

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