from PyQt6.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem, QPushButton, QApplication
from PyQt6.QtGui import QIntValidator

from models.Class import Class
from ui.Admin.AdminMainWindow import Ui_AdminManagement
from models.Student import Student
from models.Teacher import Teacher
from libs.JsonFileFactory import JsonFileFactory
from libs.DataConnector import DataConnector
from models.User import User
import os
import json
from PyQt6.QtCore import QDate, Qt

class AdminMainWindowExt(QMainWindow, Ui_AdminManagement):
    def __init__(self, admin_window):
        super().__init__()  # ✅ Gọi init của QMainWindow

        self.dc = DataConnector()
        self.students = []
        self.teachers = []
        self.admin_window = admin_window  # ✅ Giữ tham chiếu đến StudentMainWindow

        # ✅ Định nghĩa các biến TRƯỚC KHI gọi setupUi()
        self.teacher_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/teachers.json"))
        self.student_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/students.json"))
        self.class_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/classes.json"))

        self.setupUi(self)  # ✅ Gọi setup UI sau khi đã có biến cần thiết

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.jff = JsonFileFactory()
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # setup trước cho giao diện khi mưo rlên
        self.LineEdit_StuCourse.setValidator(QIntValidator(2000, 2100))
        self.load_teacher_classes_to_stuclass()
        self.update_student_advisor()
        self.comboBox_StuMajor.setEditable(True)
        self.comboBox_StuMajor.setStyleSheet("""
            QComboBox {
                border: 1px solid gray;
                border-radius: 15px; /* Bo tròn cả 4 góc */
                padding: 10px;
                font: 500 15px "Cambria";
                background: white;
                padding-right: 30px; /* Chừa khoảng trống bên phải */
            }

            QComboBox QAbstractItemView {
                border: 1px solid gray;
                selection-background-color: lightgray;
            }

            QComboBox::down-arrow {
                image: url('your_arrow_icon.png'); /* Đổi mũi tên nếu cần */
                width: 15px;
                height: 15px;
            }

            QComboBox::drop-down {
                border: none;
                subcontrol-origin: padding;
                subcontrol-position: right;
                width: 30px;
            }
        """)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Lấy thư mục hiện tại
        self.student_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/students.json"))
        self.teacher_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/teachers.json"))
        self.class_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/classes.json"))

        # Tạo thư mục dataset nếu chưa có
        dataset_folder = os.path.dirname(self.student_file)
        if not os.path.exists(dataset_folder):
            os.makedirs(dataset_folder)
            print(f"📂 Tạo thư mục: {dataset_folder}")

        # Nếu file students.json chưa tồn tại, tạo file rỗng
        if not os.path.exists(self.student_file):
            with open(self.student_file, "w", encoding="utf-8") as file:
                file.write("[]")  # Mảng trống để tránh lỗi khi đọc
            print(f"📄 Tạo file: {self.student_file}")

        # Load dữ liệu khi mở app
        self.load_students()
        self.load_teachers()
        self.load_classes()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_StuAddInfo.clicked.connect(self.process_add_student)
        self.pushButton_TeaAddInfo.clicked.connect(self.process_add_teacher)
        self.pushButton_CreateClass.clicked.connect(self.open_create_class)
        self.lineEdit_StuFullname.textChanged.connect(self.update_student_email)
        self.lineEdit_TeaFullname.textChanged.connect(self.update_teacher_email)
        self.comboBox_StuClass.currentIndexChanged.connect(self.update_student_advisor)
        #các định dạng viết hoa
        self.lineEdit_StuFullname.textChanged.connect(self.capitalize_each_word_fullname)
        self.lineEdit_TeaFullname.textChanged.connect(self.capitalize_each_word_fullname)

        self.lineEdit_StuId.textChanged.connect(self.capitalize_id_and_class)
        self.comboBox_StuClass.currentTextChanged.connect(self.capitalize_id_and_class)
        self.lineEdit_TeaId.textChanged.connect(self.capitalize_id_and_class)
        self.lineEdit_TeaClass.textChanged.connect(self.capitalize_id_and_class)
        #exit
        self.pushButton_exit.clicked.connect(self.process_exit)
        self.pushButton_exit_2.clicked.connect(self.process_exit)
        self.pushButton_exit_3.clicked.connect(self.process_exit)

    def open_create_class(self):
        self.close()
        from ui.Admin.CreateClassEx import CreateClassExt
        create_class_window = CreateClassExt()
        create_class_window.show()

    def load_teacher_classes_to_stuclass(self):
        teachers = self.jff.read_data(self.teacher_file, Teacher) or []
        classes = list(set(teacher.teacher_class for teacher in teachers if teacher.teacher_class))

        self.comboBox_StuClass.clear()
        self.comboBox_StuClass.addItems(classes)

    def process_add_student(self):
        # Đọc dữ liệu từ file JSON
        students_data = self.jff.read_data(self.student_file, dict) or []
        print(f"📂 Đọc dữ liệu thành công! Số lượng sinh viên hiện có: {len(students_data)}")

        # Lấy dữ liệu từ giao diện
        stuid = self.lineEdit_StuId.text().strip()
        name = self.lineEdit_StuFullname.text().strip()
        birthday = self.dateEdit_StuBir.date().toString("dd/MM/yyyy")  # Chuyển ngày thành dd/MM/yyyy
        gender = self.comboBox_StuGender.currentText().strip()
        email = self.lineEdit_StuMail.text().strip()
        course = self.LineEdit_StuCourse.text().strip()
        major = self.comboBox_StuMajor.currentText().strip()
        cl = self.comboBox_StuClass.currentText().strip()
        advisor = self.LineEdit_StuAdvisor.text().strip()

        print(f"📋 Dữ liệu nhập: {stuid}, {name}, {birthday}, {gender}, {email}, {course}, {major}, {cl}, {advisor}")

        if not all([stuid, name, birthday, gender, email, course, major, cl, advisor]):
            print("❌ Lỗi: Dữ liệu không đầy đủ!")
            QMessageBox.warning(self.MainWindow, "Error", "Vui lòng điền đầy đủ thông tin sinh viên!")
            return

        if not self.validate_advisor(advisor):
            print("❌ Giáo viên không tồn tại!")
            QMessageBox.warning(self.MainWindow, "Error", "Giáo viên không tồn tại!")
            return

        # Kiểm tra nếu ID đã tồn tại
        student_exists = next((student for student in students_data if student["user_id"] == stuid), None)

        if student_exists:
            # Hỏi người dùng có muốn cập nhật không
            reply = QMessageBox.question(
                self.MainWindow,
                "Xác nhận cập nhật",
                f"Học sinh có ID {stuid} đã tồn tại.\nBạn có muốn cập nhật thông tin không?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if reply == QMessageBox.StandardButton.No:
                print("🚫 Hủy cập nhật. Xóa ID nhập vào.")
                self.lineEdit_StuId.clear()  # Xóa ID để người dùng nhập lại
                return

            print(f"🔄 Cập nhật thông tin sinh viên có ID: {stuid}")
            for i, student in enumerate(students_data):
                if student["user_id"] == stuid:
                    students_data[i] = {
                        "user_id": stuid,
                        "fullname": name,
                        "birthday": birthday,
                        "gender": gender,
                        "email": email,
                        "password": student["password"],  # Giữ nguyên mật khẩu
                        "student_class": cl,
                        "major": major,
                        "course": course,
                        "advisor": advisor,
                        "registered_classes": student["registered_classes"],  # Giữ nguyên các lớp đã đăng ký
                        "grades": student["grades"]  # Giữ nguyên điểm số
                    }
                    break
            QMessageBox.information(self.MainWindow, "Success", "Thông tin học sinh đã được cập nhật!")

        else:
            new_student = {
                "user_id": stuid,
                "fullname": name,
                "birthday": birthday,
                "gender": gender,
                "email": email,
                "password": "12345",
                "student_class": cl,
                "major": major,
                "course": course,
                "advisor": advisor,
                "registered_classes": [],
                "grades": {}
            }
            print(f"✅ Thêm mới sinh viên: {new_student}")
            students_data.append(new_student)
            QMessageBox.information(self.MainWindow, "Success", "Thêm học sinh mới thành công!")

        # 🛠 Ghi file JSON
            with open(self.student_file, "w", encoding="utf-8") as file:
                json.dump(students_data, file, indent=4, ensure_ascii=False)
            print("💾 Dữ liệu đã được ghi vào JSON!")

            # ✅ Xóa nội dung form nhập liệu & Cập nhật danh sách sinh viên
            self.clear_student_form()
            self.tableWidget_Student.setRowCount(0)  # 🔄 Xóa toàn bộ dữ liệu cũ trước khi tải mới
            self.load_students()

    def process_add_teacher(self):
        print("🔍 Bắt đầu thêm giảng viên...")

        # Đọc dữ liệu từ file JSON
        teachers_data = self.jff.read_data(self.teacher_file, dict) or []
        print(f"📂 Đọc dữ liệu thành công! Số lượng giảng viên hiện có: {len(teachers_data)}")

        # Lấy dữ liệu từ giao diện
        teaid = self.lineEdit_TeaId.text().strip()
        name = self.lineEdit_TeaFullname.text().strip()
        birthday = self.dateEdit_TeaBir.date().toString("dd/MM/yyyy")  # Định dạng ngày
        gender = self.comboBox_TeaGender.currentText().strip()
        email = self.lineEdit_TeaMail.text().strip()
        faculty = self.lineEdit_TeaFaculty.text().strip()
        cl = self.lineEdit_TeaClass.text().strip()

        print(f"📋 Dữ liệu nhập: {teaid}, {name}, {birthday}, {gender}, {email}, {faculty}, {cl}")

        if not all([teaid, name, birthday, gender, email, faculty]):
            print("❌ Lỗi: Dữ liệu không đầy đủ!")
            QMessageBox.warning(self.MainWindow, "Error", "Vui lòng điền đầy đủ thông tin giảng viên!")
            return

        # Kiểm tra nếu ID đã tồn tại
        teacher_exists = next((teacher for teacher in teachers_data if teacher["user_id"] == teaid), None)

        if teacher_exists:
            # Hỏi người dùng có muốn cập nhật không
            reply = QMessageBox.question(
                self.MainWindow,
                "Xác nhận cập nhật",
                f"Giảng viên có ID {teaid} đã tồn tại.\nBạn có muốn cập nhật thông tin không?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if reply == QMessageBox.StandardButton.No:
                print("🚫 Hủy cập nhật. Xóa ID nhập vào.")
                self.lineEdit_TeaId.clear()  # Xóa ID để người dùng nhập lại
                return

            print(f"🔄 Cập nhật thông tin giảng viên có ID: {teaid}")
            for i, teacher in enumerate(teachers_data):
                if teacher["user_id"] == teaid:
                    teachers_data[i] = {
                        "user_id": teaid,
                        "fullname": name,
                        "birthday": birthday,
                        "gender": gender,
                        "email": email,
                        "password": teacher["password"],  # Giữ nguyên mật khẩu
                        "faculty": faculty,
                        "teacher_class": cl,
                        "assigned_classes": teacher["assigned_classes"]  # Giữ nguyên lớp đã được giao
                    }
                    break
            QMessageBox.information(self.MainWindow, "Success", "Thông tin giảng viên đã được cập nhật!")

        else:
            new_teacher = {
                "user_id": teaid,
                "fullname": name,
                "birthday": birthday,
                "gender": gender,
                "email": email,
                "password": "12345",
                "faculty": faculty,
                "teacher_class": cl,
                "assigned_classes": []
            }
            print(f"✅ Thêm mới giảng viên: {new_teacher}")
            teachers_data.append(new_teacher)
            QMessageBox.information(self.MainWindow, "Success", "Thêm giảng viên mới thành công!")

        # 🛠 Ghi file JSON
            with open(self.teacher_file, "w", encoding="utf-8") as file:
                json.dump(teachers_data, file, indent=4, ensure_ascii=False)
            print("💾 Dữ liệu đã được ghi vào JSON!")

            # ✅ Xóa nội dung form nhập liệu & Cập nhật danh sách giảng viên
            self.clear_teacher_form()
            self.tableWidget_Teacher.setRowCount(0)  # 🔄 Xóa toàn bộ dữ liệu cũ trước khi tải mới
            self.load_teachers()

            # ✅ Cập nhật danh sách lớp học trong comboBox_StuClass
            self.load_teacher_classes_to_stuclass()
            #hiển thị giáo viên le combobox của createclass
            from ui.Admin.CreateClassEx import CreateClassExt
            CreateClassExt.load_teacher_from_json()

    def clear_student_form(self):
        self.lineEdit_StuId.clear()
        self.lineEdit_StuFullname.clear()
        self.dateEdit_StuBir.setDate(QDate.currentDate())  # Đặt lại ngày về hôm nay
        self.comboBox_StuGender.setCurrentIndex(0)  # Chọn lại mục đầu tiên
        self.lineEdit_StuMail.clear()
        self.LineEdit_StuCourse.clear()
        self.comboBox_StuMajor.clear()
        self.comboBox_StuClass.clear()
        self.LineEdit_StuAdvisor.clear()

        print("🧹 Đã reset form nhập liệu!")  # Debug check

    def clear_teacher_form(self):
        """Xóa toàn bộ nội dung trong form nhập giảng viên."""
        self.lineEdit_TeaId.clear()
        self.lineEdit_TeaFullname.clear()
        self.dateEdit_TeaBir.setDate(QDate.currentDate())  # Đặt lại ngày về hôm nay
        self.comboBox_TeaGender.setCurrentIndex(0)  # Reset về lựa chọn đầu tiên
        self.lineEdit_TeaMail.clear()
        self.lineEdit_TeaFaculty.clear()
        self.lineEdit_TeaClass.clear()

        print("🧹 Đã reset form nhập liệu giảng viên!")  # Debug check

    def capitalize_each_word_fullname(self):
        # Student Fullname
        stu_text = self.lineEdit_StuFullname.text()
        stu_capitalized = stu_text.title()
        self.lineEdit_StuFullname.blockSignals(True)
        self.lineEdit_StuFullname.setText(stu_capitalized)
        self.lineEdit_StuFullname.blockSignals(False)

        # Teacher Fullname
        tea_text = self.lineEdit_TeaFullname.text()
        tea_capitalized = tea_text.title()
        self.lineEdit_TeaFullname.blockSignals(True)
        self.lineEdit_TeaFullname.setText(tea_capitalized)
        self.lineEdit_TeaFullname.blockSignals(False)

    def capitalize_id_and_class(self):
        self.lineEdit_StuId.setText(self.lineEdit_StuId.text().upper())
        self.comboBox_StuClass.setCurrentText(self.comboBox_StuClass.currentText().upper())
        self.lineEdit_TeaId.setText(self.lineEdit_TeaId.text().upper())
        self.lineEdit_TeaClass.setText(self.lineEdit_TeaClass.text().upper())

    def update_student_email(self):
        fullname = self.lineEdit_StuFullname.text()
        if fullname:
            email = User.generate_email(fullname, "student")
            self.lineEdit_StuMail.setText(email)

    def update_teacher_email(self):
        fullname = self.lineEdit_TeaFullname.text()
        if fullname:
            email = User.generate_email(fullname, "teacher")
            self.lineEdit_TeaMail.setText(email)

    def update_student_advisor(self):
        student_class = self.comboBox_StuClass.currentText().strip()
        print(f"📌 Nhập lớp: {student_class}")

        if not student_class:
            self.LineEdit_StuAdvisor.clear()
            print("🚫 Không có lớp, xóa Advisor!")
            return

        try:
            teachers_data = self.jff.read_data(self.teacher_file, dict) or []
            if not isinstance(teachers_data, list):  # Kiểm tra lại dữ liệu giảng viên
                print("❌ Dữ liệu giảng viên không hợp lệ!")
                return
        except Exception as e:
            print(f"❌ Lỗi khi đọc dữ liệu giảng viên: {e}")
            return

        matching_teachers = [
            teacher.get("fullname", "Không rõ") for teacher in teachers_data
            if teacher.get("teacher_class", "").strip() == student_class
        ]

        advisor_name = matching_teachers[0] if matching_teachers else ""
        print(f"📢 Advisor: {advisor_name}")

        self.LineEdit_StuAdvisor.setText(advisor_name)

    def validate_advisor(self, advisor_name):
        teachers = self.jff.read_data(self.teacher_file, Teacher) or []
        teacher_names = [teacher.fullname for teacher in teachers]
        return advisor_name in teacher_names

#quản lý ta khoản  hsinh gv
    def load_students(self):
        students = self.jff.read_data(self.student_file, Student) or []
        self.tableWidget_Student.setRowCount(len(students))
        self.tableWidget_Student.setColumnCount(9)
        self.tableWidget_Student.setHorizontalHeaderLabels(
            ["ID", "Name", "Birthday", "Gender", "Email", "Course", "Major", "Class", "Advisor"]
        )
        self.tableWidget_Student.setColumnWidth(0, 80)
        self.tableWidget_Student.setColumnWidth(1, 200)
        self.tableWidget_Student.setColumnWidth(2, 150)
        self.tableWidget_Student.setColumnWidth(3, 100)
        self.tableWidget_Student.setColumnWidth(4, 250)
        self.tableWidget_Student.setColumnWidth(5, 100)
        self.tableWidget_Student.setColumnWidth(6, 300)
        self.tableWidget_Student.setColumnWidth(7, 150)
        self.tableWidget_Student.setColumnWidth(8, 200)

        for row, student in enumerate(students):
            self.tableWidget_Student.setItem(row, 0, QTableWidgetItem(str(getattr(student, "user_id", ""))))
            self.tableWidget_Student.setItem(row, 1, QTableWidgetItem(str(getattr(student, "fullname", ""))))
            self.tableWidget_Student.setItem(row, 2, QTableWidgetItem(str(getattr(student, "birthday", ""))))
            self.tableWidget_Student.setItem(row, 3, QTableWidgetItem(str(getattr(student, "gender", ""))))
            self.tableWidget_Student.setItem(row, 4, QTableWidgetItem(str(getattr(student, "email", ""))))
            self.tableWidget_Student.setItem(row, 5, QTableWidgetItem(str(getattr(student, "course", ""))))
            self.tableWidget_Student.setItem(row, 6, QTableWidgetItem(str(getattr(student, "major", ""))))
            self.tableWidget_Student.setItem(row, 7, QTableWidgetItem(str(getattr(student, "student_class", ""))))
            self.tableWidget_Student.setItem(row, 8, QTableWidgetItem(str(getattr(student, "advisor", ""))))

        print(f"✅ Tải danh sách sinh viên thành công! Số lượng: {len(students)}")

    def load_teachers(self):
        teachers = self.jff.read_data(self.teacher_file, Teacher) or []
        self.tableWidget_Teacher.setRowCount(len(teachers))
        self.tableWidget_Teacher.setColumnCount(7)
        self.tableWidget_Teacher.setHorizontalHeaderLabels(
            ["ID", "Name", "Birthday", "Gender", "Email", "Faculty", "Class"]
        )

        self.tableWidget_Teacher.setColumnWidth(0, 80)
        self.tableWidget_Teacher.setColumnWidth(1, 200)
        self.tableWidget_Teacher.setColumnWidth(2, 100)
        self.tableWidget_Teacher.setColumnWidth(3, 100)
        self.tableWidget_Teacher.setColumnWidth(4, 250)
        self.tableWidget_Teacher.setColumnWidth(5, 300)
        self.tableWidget_Teacher.setColumnWidth(6, 100)

        for row, teacher in enumerate(teachers):
            self.tableWidget_Teacher.setItem(row, 0, QTableWidgetItem(str(getattr(teacher, "user_id", ""))))
            self.tableWidget_Teacher.setItem(row, 1, QTableWidgetItem(str(getattr(teacher, "fullname", ""))))
            self.tableWidget_Teacher.setItem(row, 2, QTableWidgetItem(str(getattr(teacher, "birthday", ""))))
            self.tableWidget_Teacher.setItem(row, 3, QTableWidgetItem(str(getattr(teacher, "gender", ""))))
            self.tableWidget_Teacher.setItem(row, 4, QTableWidgetItem(str(getattr(teacher, "email", ""))))
            self.tableWidget_Teacher.setItem(row, 5, QTableWidgetItem(str(getattr(teacher, "faculty", ""))))
            self.tableWidget_Teacher.setItem(row, 6, QTableWidgetItem(str(getattr(teacher, "teacher_class", ""))))

#quản lý lớp
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

    def show_teacher_info(self, row, column):
        if column == 4:  # Cột Teacher ID
            teacher_id = self.tableWidget_Classes.item(row, column).data(Qt.ItemDataRole.UserRole)
            teachers = self.jff.read_data(self.teacher_file, Teacher) or []
            teacher_info = next((t for t in teachers if t.user_id == teacher_id), None)

            if teacher_info:
                QMessageBox.information(
                    self.MainWindow,
                    "Thông Tin Giảng Viên",
                    f"ID: {teacher_info.user_id}\n"
                    f"Họ và Tên: {teacher_info.fullname}\n"
                    f"Khoa: {teacher_info.faculty}\n"
                    f"Email: {teacher_info.email}\n"
                )

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
            self.close()