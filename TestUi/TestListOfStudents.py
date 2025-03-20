import sys
from PyQt6.QtWidgets import QApplication
from ui.Admin.ListOfStudentsEx import ListOfStudentsWindow
from models.Class import Class  # Import class để sử dụng

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Tạo một lớp học với class_id cụ thể
    my_class = Class("C001", "TeacherName", "Room101", "Monday 9AM", "Math", "Science", 10, 30)

    # Lấy class_id từ instance của class
    list_stu_window = ListOfStudentsWindow(my_class.class_id)
    list_stu_window.show()

    sys.exit(app.exec())
