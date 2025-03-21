from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QCheckBox, QHeaderView, QTableWidget, QMainWindow, \
    QPushButton
from ui.Teacher.TeacherMainWindow import Ui_MainWindow
from libs.JsonFileFactory import JsonFileFactory

import os
import json

class TeacherMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.jff = JsonFileFactory()
        self.setupSignalAndSlot()

        # 🛠 Lấy đường dẫn thư mục gốc (FinalTerm)
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

        self.class_file = os.path.join(base_dir, "dataset", "classes.json")
        self.teacher_file = os.path.join(base_dir, "dataset", "teachers.json")
        self.student_file = os.path.join(base_dir, "dataset", "students.json")

        # 🔍 Debug để kiểm tra đường dẫn
        print(f"📂 [DEBUG] Đường dẫn class_file: {self.class_file}")
        print(f"📂 [DEBUG] Đường dẫn teacher_file: {self.teacher_file}")

        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_exit.clicked.connect(self.process_exit)
        self.pushButton_logout.clicked.connect(self.process_logout)

    def process_logout(self):
        reply = QMessageBox.question(
            self.MainWindow,
            "Logout Confirmation",
            "Are you sure you want to return to the login page?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        from ui.LoginMainWindow.LoginMainWindowEx import LoginMainWindowExt

        if reply == QMessageBox.StandardButton.Yes:
            self.login_window = QMainWindow()  # Lưu vào self để không bị hủy ngay lập tức
            self.login_ui = LoginMainWindowExt()
            self.login_ui.setupUi(self.login_window)
            self.login_ui.showWindow()

            self.MainWindow.close()  # Đóng cửa sổ hiện tại

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

    def load_assigned_classes(self, user_email):
        """Load danh sách lớp học được phân công của giáo viên và cập nhật vào bảng"""

        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        teacher_file = os.path.join(base_dir, "dataset", "teachers.json")
        class_file = os.path.join(base_dir, "dataset", "classes.json")

        if not os.path.exists(teacher_file) or not os.path.exists(class_file):
            QMessageBox.critical(self.MainWindow, "Error", "Không tìm thấy file dữ liệu lớp học!")
            return

        try:
            # 📌 Đọc dữ liệu giáo viên
            with open(teacher_file, "r", encoding="utf-8") as file:
                teachers_data = json.load(file)

            # 🔍 Tìm giáo viên theo email
            teacher = next((t for t in teachers_data if t.get("email") == user_email), None)
            if not teacher:
                QMessageBox.warning(self.MainWindow, "Warning", "Không tìm thấy giáo viên!")
                return

            assigned_classes_names = teacher.get("assigned_classes", [])  # Danh sách TÊN lớp
            print(f"📚 [DEBUG] Lớp học được phân công (Tên): {assigned_classes_names}")

            # 📌 Đọc dữ liệu lớp học từ classes.json
            with open(class_file, "r", encoding="utf-8") as file:
                classes_data = json.load(file)

            # 🔍 Đổi tên lớp thành class_id
            assigned_class_ids = [
                cls["class_id"] for cls in classes_data if cls["subject"] in assigned_classes_names
            ]
            print(f"🔄 [DEBUG] Chuyển đổi Tên lớp → class_id: {assigned_class_ids}")

            # 🔍 Lọc danh sách lớp theo class_id
            assigned_classes = [
                cls for cls in classes_data if cls.get("class_id") in assigned_class_ids
            ]

            print(f"📊 [DEBUG] Lớp học đầy đủ thông tin: {assigned_classes}")

            # Nếu vẫn rỗng, báo lỗi để debug
            if not assigned_classes:
                QMessageBox.warning(self.MainWindow, "Warning", "Không tìm thấy lớp học phù hợp!")
                return

            # ✨ Cập nhật bảng
            self.tableWidget_classes.setRowCount(len(assigned_classes))
            self.tableWidget_classes.setColumnCount(5)
            self.tableWidget_classes.setHorizontalHeaderLabels(
                ["Class ID", "Subject", "Room", "Schedule", "List of Students"]
            )

            self.tableWidget_classes.setColumnWidth(1, 200)  # Subject
            self.tableWidget_classes.setColumnWidth(2, 100)  # Room
            self.tableWidget_classes.setColumnWidth(3, 244)  # Schedule
            self.tableWidget_classes.setColumnWidth(4, 200)  # Teacher ID

            # Thêm dữ liệu vào bảng
            for row, cls in enumerate(assigned_classes):
                self.tableWidget_classes.insertRow(row)

                self.tableWidget_classes.setItem(row, 0, QTableWidgetItem(cls["class_id"]))
                self.tableWidget_classes.setItem(row, 1, QTableWidgetItem(cls["subject"]))
                self.tableWidget_classes.setItem(row, 2, QTableWidgetItem(cls["room"]))
                self.tableWidget_classes.setItem(row, 3, QTableWidgetItem(cls["schedule"]))

                # 👉 Thêm nút "List of Students"
                btn = QPushButton("List of Students")
                btn.setStyleSheet("""
                                QPushButton {
                                    font: 800 12pt "Cambria";
                                    background-color: rgba(0,0,90,100);
                                    color: rgb(0,0,90);
                                    padding: 3px; /* Khoảng cách giữa chữ và viền */
                                    border: 1px solid rgba(255, 255,255, 200); /* Viền đỏ đậm */
                                }

                                QPushButton:hover {
                                    background-color: rgb(0,0,90); 
                                    color: rgb(255,255,255);
                                }

                                QPushButton:pressed {
                                    background-color: rgb(0, 0,9);
                                    color: rgb(255,255,255);
                                }
                            """)
                btn.setFixedSize(200, 30)  # Đặt chiều rộng và cao hợp lý
                btn.clicked.connect(lambda _, cid=cls["class_id"]: self.show_student_list(cid))
                self.tableWidget_classes.setCellWidget(row, 4, btn)

            print("✅ [DEBUG] Cập nhật danh sách lớp học thành công!")

        except Exception as e:
            print(f"❌ [ERROR] Lỗi khi xử lý danh sách lớp: {e}")
            QMessageBox.critical(self.MainWindow, "Error", f"Lỗi khi xử lý dữ liệu: {e}")

    def show_student_list(self, class_id):
        """Mở danh sách sinh viên của lớp và đóng cửa sổ hiện tại"""
        from ui.Teacher.ListOfStudentsEx import ListOfStudentsWindow

        # 🔥 Đọc danh sách sinh viên từ JSON
        students_data = self.jff.read_data(self.student_file, dict) or []
        classes_data = self.jff.read_data(self.class_file, dict) or []

        # 🔥 Tìm lớp học theo `class_id`
        class_info = None
        for c in classes_data:
            if c["class_id"] == class_id:
                class_info = c
                break

        if not class_info:
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Không tìm thấy lớp {class_id} trong hệ thống!")
            return

        # 🔥 Lấy danh sách `user_id` của sinh viên đã đăng ký lớp (Dùng `list` thay vì `set`)
        student_ids = class_info.get("students", [])  # Dùng `list`, không loại bỏ trùng

        # 🔥 Lọc danh sách sinh viên theo ID
        enrolled_students = [s for s in students_data if s.get("user_id") in student_ids]

        if not enrolled_students:
            QMessageBox.warning(self.MainWindow, "Danh Sách Trống", f"Lớp {class_id} hiện chưa có học sinh đăng ký.")
            return

        self.student_windows = getattr(self, "student_windows", [])  # 🔥 Tạo danh sách lưu cửa sổ
        self.student_list_window = ListOfStudentsWindow(class_id, enrolled_students)
        self.student_windows.append(self.student_list_window)  # 🔥 Giữ tham chiếu để không bị xóa
        self.student_list_window.show()