# Form implementation generated from reading ui file 'D:\Documents\KTLT\FinalTerm\ui\Admin\ListOfStudents.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Documents\\KTLT\\FinalTerm\\ui\\Admin\\../../../../../Downloads/Purple and White Modern Login and Sign-up Website Page UI Desktop Prototype (1000 x 710 px) (1000 x 710 px) (1000 x 712 px) (1000 x 600 px).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
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
        self.listWidget_Students = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        self.listWidget_Students.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget_Students.setMaximumSize(QtCore.QSize(16777215, 500))
        self.listWidget_Students.setStyleSheet("    QListWidget {\n"
"        border: 2px solid rgb(255,255,255);\n"
"        background-color: white;\n"
"        padding: 5px;\n"
"    }")
        self.listWidget_Students.setObjectName("listWidget_Students")
        self.verticalLayout.addWidget(self.listWidget_Students)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Home = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_Home.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_Home.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_Home.setStyleSheet("QPushButton {\n"
"    font: 5000 14pt \"Arial\"; /* Font Arial Black, size 12 */\n"
"    background-color: rgba(170,0,0,150); /* Màu nền đỏ đậm */\n"
"    color: rgb(255,255,255); /* Màu chữ trắng */\n"
"    border-bottom-left-radius: 20px;\n"
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
        self.pushButton_Home.setObjectName("pushButton_Home")
        self.horizontalLayout.addWidget(self.pushButton_Home)
        self.pushButton_AssignStudent = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_AssignStudent.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_AssignStudent.setStyleSheet("QPushButton {\n"
"    font: 5000 14pt \"Arial\"; /* Font Arial Black, size 12 */\n"
"    background-color: rgba(0,85,0,100); /* Màu nền đỏ đậm */\n"
"    color: rgb(0, 85, 0); /* Màu chữ trắng */\n"
"    border-bottom-right-radius: 20px;\n"
"    padding: 8px; /* Khoảng cách giữa chữ và viền */\n"
"    border: 4px solid rgba(255, 255,255, 200); /* Viền đỏ đậm */\n"
"    box-shadow: 3px 3px 8px rgba(0, 0, 0, 100); /* Đổ bóng */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(0, 109, 80); /* Màu sáng hơn khi hover */\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0,85,0); /* Màu tối hơn khi nhấn */\n"
"    color: rgb(255,255,255);\n"
"    box-shadow: 1px 1px 5px rgba(0, 0, 0, 150); /* Giảm bóng khi nhấn */\n"
"}")
        self.pushButton_AssignStudent.setObjectName("pushButton_AssignStudent")
        self.horizontalLayout.addWidget(self.pushButton_AssignStudent)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "List of Students"))
        self.label_3.setText(_translate("Dialog", "LIST OF STUDENTS"))
        self.pushButton_Home.setText(_translate("Dialog", "BACK"))
        self.pushButton_AssignStudent.setText(_translate("Dialog", "SAVE"))
