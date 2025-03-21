import json
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from ui.Teacher.TeacherMainWindow import Ui_MainWindow  # Import UI giao diện giáo viên


class TeacherMainWindowEx(QMainWindow, Ui_MainWindow):
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


    def load_classes(self):
        classes = self.jff.read_data(self.class_file, Class) or []
        self.tableWidget_Classes.setRowCount(len(classes))
        self.tableWidget_Classes.setColumnCount(6)  # Thêm cột "List of Students"
        self.tableWidget_Classes.setHorizontalHeaderLabels(
            ["Class ID", "Subject", "Room", "Schedule", "Teacher", "List of Students"]
        )

        self.tableWidget_Classes.setColumnWidth(1, 200)  # Subject
        self.tableWidget_Classes.setColumnWidth(2, 100)  # Room
        self.tableWidget_Classes.setColumnWidth(3, 266)  # Schedule
        self.tableWidget_Classes.setColumnWidth(4, 100)  # Teacher ID
        self.tableWidget_Classes.setColumnWidth(5, 200)  # List of Students Button

        for row, cls in enumerate(classes):
            self.tableWidget_Classes.setItem(row, 0, QTableWidgetItem(cls.class_id))
            self.tableWidget_Classes.setItem(row, 1, QTableWidgetItem(cls.subject))
            self.tableWidget_Classes.setItem(row, 2, QTableWidgetItem(cls.room))
            self.tableWidget_Classes.setItem(row, 3, QTableWidgetItem(cls.schedule))

            teacher_id_item = QTableWidgetItem(cls.teacher)
            self.tableWidget_Classes.setItem(row, 4, teacher_id_item)
            teacher_id_item.setFlags(teacher_id_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            teacher_id_item.setData(Qt.ItemDataRole.UserRole, cls.teacher)

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
            btn.clicked.connect(lambda _, cid=cls.class_id: self.show_student_list(cid))
            self.tableWidget_Classes.setCellWidget(row, 5, btn)

        self.tableWidget_Classes.cellClicked.connect(self.show_teacher_info)

    def show_student_list(self, class_id):
        """Mở danh sách sinh viên của lớp và đóng cửa sổ hiện tại"""
        from ui.Admin.ListOfStudentsEx import ListOfStudentsWindow

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
            QMessageBox.warning(self, "Lỗi", f"Không tìm thấy lớp {class_id} trong hệ thống!")
            return

        # 🔥 Lấy danh sách `user_id` của sinh viên đã đăng ký lớp (Dùng `list` thay vì `set`)
        student_ids = class_info.get("students", [])  # Dùng `list`, không loại bỏ trùng

        # 🔥 Lọc danh sách sinh viên theo ID
        enrolled_students = [s for s in students_data if s.get("user_id") in student_ids]

        if not enrolled_students:
            QMessageBox.warning(self, "Danh Sách Trống", f"Lớp {class_id} hiện chưa có học sinh đăng ký.")
            return

        self.close()  # 🔥 Đóng cửa sổ hiện tại trước khi mở cửa sổ mới

        self.student_windows = getattr(self, "student_windows", [])  # 🔥 Tạo danh sách lưu cửa sổ
        self.student_list_window = ListOfStudentsWindow(class_id, enrolled_students)
        self.student_windows.append(self.student_list_window)  # 🔥 Giữ tham chiếu để không bị xóa
        self.student_list_window.show()