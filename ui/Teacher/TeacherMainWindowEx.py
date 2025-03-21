import json
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from ui.Teacher.TeacherMainWindow import Ui_MainWindow  # Import UI giao diện giáo viên


class TeacherMainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self, email):
        super().__init__()
        self.email = email  # Nhận email từ hệ thống đăng nhập
        print(f"📌 [DEBUG] Email nhận vào: {self.email}")

        self.user_id = self.get_teacher_id_by_email(email)  # Lấy user_id từ email
        print(f"📌 [DEBUG] User ID tìm được: {self.user_id}")

        if self.user_id is None:
            QMessageBox.critical(self, "Lỗi", "Không tìm thấy giáo viên với email này!")
            print("❌ [DEBUG] Không tìm thấy giáo viên!")
            self.close()
            return

        self.setupUi(self)  # Khởi tạo giao diện
        self.load_classes()  # Load danh sách lớp khi mở giao diện
        self.pushButton_logout.clicked.connect(self.logout)  # Xử lý đăng xuất

    def get_teacher_id_by_email(self, email):
        """ Tìm teacher_id dựa vào email trong file teachers.json """
        try:
            print("📌 [DEBUG] Đang mở file teachers.json...")
            with open("dataset/teachers.json", "r", encoding="utf-8") as f:
                teachers = json.load(f)

            print(f"📌 [DEBUG] Số lượng giáo viên trong file: {len(teachers)}")

            for teacher in teachers:
                print(f"🔍 [DEBUG] Kiểm tra giáo viên: {teacher['email']} - ID: {teacher['teacher_id']}")
                if teacher["email"] == email:
                    print(f"✅ [DEBUG] Tìm thấy teacher_id: {teacher['teacher_id']}")
                    return teacher["teacher_id"]

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi đọc teachers.json: {e}")
            print(f"❌ [DEBUG] Lỗi khi đọc teachers.json: {e}")

        return None  # Không tìm thấy giáo viên

    def load_classes(self):
        """ Đọc danh sách lớp từ classes.json và hiển thị lên bảng """
        try:
            print("📌 [DEBUG] Đang mở file classes.json...")
            with open("dataset/classes.json", "r", encoding="utf-8") as f:
                classes = json.load(f)

            print(f"📌 [DEBUG] Số lượng lớp trong file: {len(classes)}")

            # Lọc ra các lớp do giáo viên này giảng dạy
            teacher_classes = [c for c in classes if c["teacher_id"] == self.user_id]

            print(f"📌 [DEBUG] Số lớp dạy của giáo viên {self.user_id}: {len(teacher_classes)}")

            if not teacher_classes:
                QMessageBox.information(self, "Thông báo", "Bạn không có lớp nào được phân công.")
                print("⚠️ [DEBUG] Giáo viên không có lớp nào!")
                return

            # Hiển thị danh sách lớp vào bảng
            self.tableWidget_classes.setRowCount(len(teacher_classes))
            self.tableWidget_classes.setColumnCount(2)
            self.tableWidget_classes.setHorizontalHeaderLabels(["Mã lớp", "Tên lớp"])

            for row, c in enumerate(teacher_classes):
                print(f"📌 [DEBUG] Thêm vào bảng: {c['class_id']} - {c['class_name']}")
                self.tableWidget_classes.setItem(row, 0, QTableWidgetItem(c["class_id"]))
                self.tableWidget_classes.setItem(row, 1, QTableWidgetItem(c["class_name"]))

            print("✅ [DEBUG] Load lớp học hoàn tất!")

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tải danh sách lớp: {e}")
            print(f"❌ [DEBUG] Lỗi khi tải danh sách lớp: {e}")

    def logout(self):
        """ Xử lý đăng xuất """
        print("📌 [DEBUG] Giáo viên đang đăng xuất...")
        self.close()  # Đóng giao diện giáo viên
        QMessageBox.information(self, "Đăng xuất", "Bạn đã đăng xuất thành công!")
