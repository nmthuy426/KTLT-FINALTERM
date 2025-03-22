import sys
from PyQt6.QtWidgets import QApplication
from ui.Admin.AdminMainWindowEx import AdminMainWindowExt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AdminMainWindowExt(None)
    main_window.show()
    sys.exit(app.exec())
