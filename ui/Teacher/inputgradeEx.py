from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from libs.DataConnector import DataConnector
from libs.JsonFileFactory import JsonFileFactory
from models.Grade import Grade
from ui.Teacher.inputgrade import Ui_MainWindow  # Import UI từ file .ui đã convert


class inputgradeExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        """Thiết lập giao diện chính cho cửa sổ nhập điểm"""
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setupSignalAndSlot()
        self.dc = DataConnector()
        self.jff = JsonFileFactory()
        self.load_teacher_classes()

    def setupSignalAndSlot(self):
        self.pushButton_back.clicked.connect(self.process_back)
        self.pushButton_save.clicked.connect(self.process_save)
        self.comboBox.currentIndexChanged.connect(self.update_table)

    def showWindow(self):
        self.MainWindow.show()

    def process_back(self):
        self.MainWindow.close()

    def load_teacher_classes(self):
        """Load danh sách lớp của giáo viên vào combobox"""
        teacher_id = self.get_current_teacher_id()
        if not teacher_id:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không tìm thấy thông tin giáo viên")
            return

        classes = self.dc.get_classes_by_teacher(teacher_id)
        self.comboBox.clear()
        for class_info in classes:
            self.comboBox.addItem(class_info["class_name"], class_info["class_id"])

        if self.comboBox.count() > 0:
            self.update_table()

    def get_current_teacher_id(self):
        """Lấy ID của giáo viên hiện tại"""
        user_info = self.dc.get_current_user()
        return user_info.get("teacher_id") if user_info else None

    def update_table(self):
        """Cập nhật bảng điểm theo lớp được chọn"""
        class_id = self.comboBox.currentData()
        if not class_id:
            return

        students = self.dc.get_students_by_class(class_id)
        grades = self.load_grades(class_id)
        self.tableWidget_grade.setRowCount(len(students))
        for row, student in enumerate(students):
            self.tableWidget_grade.setItem(row, 0, QTableWidgetItem(student["student_id"]))
            self.tableWidget_grade.setItem(row, 1, QTableWidgetItem(student["student_name"]))
            student_grade = grades.get(student["student_id"], Grade(student["student_id"], class_id))
            self.tableWidget_grade.setItem(row, 2, QTableWidgetItem(str(student_grade.formative1)))
            self.tableWidget_grade.setItem(row, 3, QTableWidgetItem(str(student_grade.formative2)))
            self.tableWidget_grade.setItem(row, 4, QTableWidgetItem(str(student_grade.midterm)))
            self.tableWidget_grade.setItem(row, 5, QTableWidgetItem(str(student_grade.finalterm)))
            self.tableWidget_grade.setItem(row, 6, QTableWidgetItem(str(student_grade.average)))

    def load_grades(self, class_id):
        """Đọc điểm từ file"""
        grades = Grade.load_from_file()
        return {g.student_id: g for g in grades if g.class_id == class_id}

    def process_save(self):
        """Lưu điểm vào file JSON"""
        class_id = self.comboBox.currentData()
        if not class_id:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn lớp trước khi lưu")
            return

        grades = []
        for row in range(self.tableWidget_grade.rowCount()):
            student_id = self.tableWidget_grade.item(row, 0).text()
            formative1 = float(self.tableWidget_grade.item(row, 2).text() or 0)
            formative2 = float(self.tableWidget_grade.item(row, 3).text() or 0)
            midterm = float(self.tableWidget_grade.item(row, 4).text() or 0)
            finalterm = float(self.tableWidget_grade.item(row, 5).text() or 0)
            grade = Grade(student_id, class_id, formative1, formative2, midterm, finalterm)
            grades.append(grade)

        Grade.save_to_file(grades)
        QMessageBox.information(self.MainWindow, "Thành công", "Lưu điểm thành công")
