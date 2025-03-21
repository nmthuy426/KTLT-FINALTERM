import os
import json
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui.Teacher.ListOfStudents import Ui_MainWindow_2  # Import UI từ file .ui đã convert

class ListOfStudentsWindow(QMainWindow, Ui_MainWindow_2):
    def __init__(self, class_id, student_list):
        """Khởi tạo cửa sổ danh sách sinh viên"""
        super().__init__()
        self.setupUi(self)  # Load giao diện từ file .ui
        self.class_id = class_id
        self.student_list = student_list  # 🔥 Lưu danh sách sinh viên
        self.grades_file = "../dataset/grades.json"  # Đường dẫn file lưu điểm

        self.setupSignalAndSlot()  # Kết nối các sự kiện
        self.load_students()  # 🔥 Load danh sách sinh viên từ `student_list`

    def setupUi(self, MainWindow):
        """Thiết lập giao diện chính cho cửa sổ danh sách sinh viên"""
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        """Kết nối các signal & slot"""
        self.pushButton_back.clicked.connect(self.process_back)
        self.pushButton_save.clicked.connect(self.save_grades)

    def showWindow(self):
        """Hiển thị cửa sổ danh sách sinh viên"""
        self.show()

    def process_back(self):
        """Đóng cửa sổ danh sách sinh viên"""
        self.close()

    def load_students(self):
        """Hiển thị danh sách sinh viên của lớp lên bảng với các cột nhập điểm"""
        print(f"📌 DEBUG: Loading students for class {self.class_id}")

        if not self.student_list:
            QMessageBox.warning(self, "Danh Sách Trống", f"Lớp {self.class_id} chưa có sinh viên đăng ký.")
            return

        self.tableWidget.setRowCount(len(self.student_list))
        self.tableWidget.setColumnCount(7)  # 2 cột thông tin + 4 cột điểm + 1 cột trung bình
        self.tableWidget.setHorizontalHeaderLabels(["Student ID", "Full Name", "Formative 1", "Formative 2", "Midterm", "Finalterm", "Average"])

        for row, student in enumerate(self.student_list):
            user_id = student.get("user_id", "Unknown")
            full_name = student.get("fullname", "No Name")

            print(f"📌 DEBUG: Adding Student - ID: {user_id}, Name: {full_name}")

            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(user_id)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(full_name)))

            # Các cột nhập điểm (mặc định là 0)
            for col in range(2, 6):
                item = QTableWidgetItem("0")
                if item:
                    self.tableWidget.setItem(row, col, item)

            # Cột điểm trung bình (không cho nhập)
            avg_item = QTableWidgetItem("0")
            avg_item.setFlags(avg_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.tableWidget.setItem(row, 6, avg_item)

        print(f"✅ DEBUG: Loaded {len(self.student_list)} students for class {self.class_id}")

    def save_grades(self):
        """Lưu điểm của sinh viên vào file JSON"""
        print(f"📌 DEBUG: Saving grades for class {self.class_id}")

        grades = []

        for row in range(self.tableWidget.rowCount()):
            student_id = self.tableWidget.item(row, 0).text() if self.tableWidget.item(row, 0) else "Unknown"
            formative1 = self.get_float_value(row, 2)
            formative2 = self.get_float_value(row, 3)
            midterm = self.get_float_value(row, 4)
            finalterm = self.get_float_value(row, 5)

            # ✅ Tính điểm trung bình
            average = round((formative1 + formative2 + midterm * 2 + finalterm * 3) / 7, 2)

            print(
                f"📌 DEBUG: Saving - ID: {student_id}, F1: {formative1}, F2: {formative2}, Mid: {midterm}, Final: {finalterm}, Avg: {average}")

            # ✅ Cập nhật cột `Average` trong bảng
            self.tableWidget.setItem(row, 6, QTableWidgetItem(str(average)))

            # ✅ Chuyển thành dictionary để lưu JSON
            grade = {
                "student_id": student_id,
                "class_id": self.class_id,
                "formative1": formative1,
                "formative2": formative2,
                "midterm": midterm,
                "finalterm": finalterm,
                "average": average
            }

            grades.append(grade)

        # ✅ Kiểm tra dữ liệu trước khi gọi `write_to_file()`
        if not grades:
            print("⚠ DEBUG: Không có dữ liệu để lưu!")
            return

        # ✅ Ghi vào file JSON
        self.write_to_file(grades)
        QMessageBox.information(self, "Thành Công", "Lưu điểm thành công!")

    def get_float_value(self, row, col):
        """Lấy giá trị điểm từ bảng, đảm bảo kiểu float"""
        item = self.tableWidget.item(row, col)
        if item:
            text_value = item.text().strip()
            print(f"📌 DEBUG: Read value at Row {row}, Col {col} → '{text_value}'")

            if text_value:
                try:
                    value = float(text_value)
                    return value
                except ValueError:
                    QMessageBox.warning(self, "Lỗi", f"Điểm của sinh viên {self.tableWidget.item(row, 0).text()} không hợp lệ!")
                    return 0.0
        return 0.0

    def write_to_file(self, new_grades):
        """Ghi danh sách điểm vào file grades.json"""
        grades_file = "../dataset/grades.json"

        # ✅ Kiểm tra file `grades.json` có tồn tại không, nếu không thì tạo file rỗng
        if not os.path.exists(grades_file):
            print(f"⚠ DEBUG: File {grades_file} không tồn tại! Đang tạo mới...")
            with open(grades_file, "w", encoding="utf-8") as file:
                json.dump([], file)

        print(f"📌 DEBUG: Writing {len(new_grades)} records to {grades_file}")

        # ✅ Đọc dữ liệu cũ (nếu có)
        existing_grades = []
        try:
            with open(grades_file, "r", encoding="utf-8") as file:
                existing_grades = json.load(file)
        except json.JSONDecodeError:
            print("⚠ DEBUG: JSON Decode Error - Xóa file lỗi và tạo mới!")
            existing_grades = []

        # ✅ Cập nhật dữ liệu cũ
        student_dict = {g["student_id"]: g for g in existing_grades}
        for grade in new_grades:
            student_dict[grade["student_id"]] = grade

        # ✅ Kiểm tra lần cuối trước khi ghi
        final_data = list(student_dict.values())
        print(f"📌 DEBUG: Final Data to Write → {final_data}")

        try:
            # ✅ Ghi lại file JSON
            with open(grades_file, "w", encoding="utf-8") as file:
                json.dump(final_data, file, indent=4)

            print(f"✅ DEBUG: Grades saved successfully to {grades_file}")

        except Exception as e:
            print(f"❌ ERROR: Failed to write file → {e}")
