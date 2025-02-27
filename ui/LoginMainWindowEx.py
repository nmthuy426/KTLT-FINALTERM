from PyQt6.QtWidgets import QMessageBox, QMainWindow

from LoginMainWindow import Ui_MainWindow

class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()