# Form implementation generated from reading ui file 'D:\Documents\KTLT\FinalTerm\ui\Admin\ListOfStudents.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 50, 881, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(956, 50))
        self.label_3.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 90);\n"
"font-weight: bold;\n"
"font: 5000 12pt \"Arial\";\n"
"border-top-left-radius: 25px;\n"
"border-top-right-radius: 25px;\n"
"padding: 10px;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget)
        self.tableWidget.setStyleSheet("    QHeaderView::section {\n"
"        background-color: rgb(0, 0, 90);  /* Màu xanh đậm */\n"
"        color: white;  /* Chữ màu trắng để dễ đọc */\n"
"        font-weight: bold;\n"
"        padding: 4px;\n"
"    }\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_back = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_back.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_back.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_back.setStyleSheet("QPushButton {\n"
"    font: 5000 14pt \"Arial\"; /* Font Arial Black, size 12 */\n"
"    background-color: rgba(170,0,0,150); /* Màu nền đỏ đậm */\n"
"    color: rgb(255,255,255); /* Màu chữ trắng */\n"
"    border-bottom-left-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"    padding: 4px; /* Khoảng cách giữa chữ và viền */\n"
"    border: 4px solid rgba(255, 255,255, 200); /* Viền đỏ đậm */\n"
"    box-shadow: 3px 3px 8px rgba(0, 0, 0, 100); /* Đổ bóng */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(170,0,0); /* Màu sáng hơn khi hover */\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(112,0,0); /* Màu tối hơn khi nhấn */\n"
"    color: rgb(255,255,255);\n"
"    box-shadow: 1px 1px 5px rgba(0, 0, 0, 150); /* Giảm bóng khi nhấn */\n"
"}")
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout.addWidget(self.pushButton_back)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Documents\\KTLT\\FinalTerm\\ui\\Admin\\../../image/Purple and White Modern Login and Sign-up Website Page UI Desktop Prototype (1000 x 710 px) (1000 x 710 px) (1000 x 712 px) (1000 x 600 px).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "LIST OF STUDENTS"))
        self.pushButton_back.setText(_translate("MainWindow", "BACK"))
