# Form implementation generated from reading ui file 'D:\Documents\KTLT\FinalTerm\ui\LoginMainWindow\LoginMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 410)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 561, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 10000 35pt \"Arial\";\n"
"background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255,255,255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 120, 521, 51))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    font: 50 12pt \"Cambria\";\n"
"    border-radius: 25px; /* Bo góc 10px */\n"
"    padding: 5px; /* Tạo khoảng cách bên trong */\n"
"    padding-left: 60px; /* Đẩy chữ vào bên phải để icon che phía trước */\n"
"    background-color: rgb(255,255,255); /* Màu nền đỏ đậm */\n"
"}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 220, 521, 51))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    font: 50 12pt \"Cambria\";\n"
"    border-radius: 25px; /* Bo góc 10px */\n"
"    padding: 5px; /* Tạo khoảng cách bên trong */\n"
"    padding-left: 60px; /* Đẩy chữ vào bên phải để icon che phía trước */\n"
"    background-color: rgb(255,255,255); /* Màu nền đỏ đậm */\n"
"}")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 111, 20))
        self.label_2.setStyleSheet("color: rgb(255,255,255);\n"
"background-color: rgba(255, 255, 255,0);\n"
"font: 2000 10pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 189, 121, 21))
        self.label_3.setStyleSheet("color: rgb(255,255,255);\n"
"background-color: rgba(255, 255, 255,0);\n"
"font: 2000 10pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 290, 281, 21))
        self.checkBox.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
"font: 2000 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255,255,255);")
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 280, 171, 41))
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
"font: 2000 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255,255,255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 330, 261, 51))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    font: 5000 14pt \"Arial\"; /* Font Arial Black, size 12 */\n"
"    background-color: rgba(255,255,255,100); /* Màu nền đỏ đậm */\n"
"    color: rgb(0,0,90); /* Màu chữ trắng */\n"
"    border-radius: 25px; /* Bo góc 20px */\n"
"    padding: 8px; /* Khoảng cách giữa chữ và viền */\n"
"    border: 4px solid rgba(255, 255,255, 200); /* Viền đỏ đậm */\n"
"    box-shadow: 3px 3px 8px rgba(0, 0, 0, 100); /* Đổ bóng */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,0,90); /* Màu sáng hơn khi hover */\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0,9); /* Màu tối hơn khi nhấn */\n"
"    color: rgb(255,255,255);\n"
"    box-shadow: 1px 1px 5px rgba(0, 0, 0, 150); /* Giảm bóng khi nhấn */\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 130, 31, 31))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("D:\\Documents\\KTLT\\FinalTerm\\ui\\LoginMainWindow\\../../image/user.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 230, 31, 31))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("D:\\Documents\\KTLT\\FinalTerm\\ui\\LoginMainWindow\\../../image/password.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "LOGIN"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Your school email"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "Username:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.checkBox.setText(_translate("MainWindow", "Save my login information"))
        self.pushButton.setText(_translate("MainWindow", "Forget password?"))
        self.pushButton_2.setText(_translate("MainWindow", "LOGIN"))
