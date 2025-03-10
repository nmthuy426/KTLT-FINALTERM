from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.Admin.AdminMainWindowEx import AdminMainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=AdminMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
