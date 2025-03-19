import sys
from PyQt6.QtWidgets import QApplication
from ui.Admin.CreateClassEx import CreateClassExt

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Tạo cửa sổ CreateClass
    create_class_window = CreateClassExt()
    create_class_window.show()

    sys.exit(app.exec())
