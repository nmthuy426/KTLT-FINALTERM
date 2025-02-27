from PyQt6.QtWidgets import QMessageBox, QMainWindow

class LoginMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Gọi setupUi đúng cách