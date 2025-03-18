import sys
from PyQt6.QtWidgets import QApplication
from ui.Admin.CreateClassEx import CreateClassExt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateClassExt()  # ✅ Tạo cửa sổ đúng cách
    window.show()  # ✅ Hiển thị cửa sổ
    sys.exit(app.exec())