# Form implementation generated from reading ui file 'D:\Documents\KTLT\FinalTerm\ui\Teacher\TeacherMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 684)
        MainWindow.setMaximumSize(QtCore.QSize(1056, 752))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.scrollArea.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 792, 641))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.scrollAreaWidgetContents)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.stackedWidget.setMaximumSize(QtCore.QSize(768, 300))
        self.stackedWidget.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(parent=self.page_2)
        self.label_2.setGeometry(QtCore.QRect(1, 0, 768, 51))
        self.label_2.setMinimumSize(QtCore.QSize(768, 0))
        self.label_2.setMaximumSize(QtCore.QSize(933, 16777215))
        self.label_2.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 90);\n"
"font-weight: bold;\n"
"font: 5000 18pt \"Arial\";\n"
"\n"
"    border-top-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    padding: 10px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.page_2)
        self.label.setGeometry(QtCore.QRect(1, 50, 768, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(768, 0))
        self.label.setMaximumSize(QtCore.QSize(933, 350))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Documents\\KTLT\\FinalTerm\\ui\\Teacher\\../../../../../Downloads/TNT_7659-scaled(1)(1).png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextEditable)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.comboBox.setMinimumSize(QtCore.QSize(768, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(768, 16777215))
        self.comboBox.setStyleSheet("    border: 1px solid gray; \n"
"    font: 2000 18px \"Cambria\";\n"
"    background: white;\n"
"    color: rgb(0, 0, 127);\n"
"    padding: 10px;\n"
"\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.listWidget = QtWidgets.QListWidget(parent=self.scrollAreaWidgetContents)
        self.listWidget.setMinimumSize(QtCore.QSize(768, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(768, 16777215))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 500 10pt \"Cambria\";\n"
"color: rgb(0, 0, 0);\n"
"/* Chỉ bo tròn hai góc trên */\n"
"    background-color: white;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"    padding: 10px;\n"
"border: 1px solid gray;\n"
"\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_exit = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_exit.setMaximumSize(QtCore.QSize(384, 50))
        self.pushButton_exit.setSizeIncrement(QtCore.QSize(0, 500))
        self.pushButton_exit.setStyleSheet("QPushButton {\n"
"    font: 5000 14pt \"Arial\"; /* Font Arial Black, size 12 */\n"
"    background-color: rgba(170,0,0,150); /* Màu nền đỏ đậm */\n"
"    color: rgb(255,255,255); /* Màu chữ trắng */\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    padding: 8px; /* Khoảng cách giữa chữ và viền */\n"
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
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout.addWidget(self.pushButton_exit)
        self.pushButton_logout = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_logout.sizePolicy().hasHeightForWidth())
        self.pushButton_logout.setSizePolicy(sizePolicy)
        self.pushButton_logout.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_logout.setMaximumSize(QtCore.QSize(384, 50))
        self.pushButton_logout.setStyleSheet("QPushButton {\n"
"    font: 5000 14pt \"Arial\"; /* Font Arial Black, size 12 */\n"
"    background-color: rgba(255,255,255,100); /* Màu nền đỏ đậm */\n"
"    color: rgb(0,0,90); /* Màu chữ trắng */\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
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
        self.pushButton_logout.setIconSize(QtCore.QSize(50, 20))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.horizontalLayout.addWidget(self.pushButton_logout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TEACHER"))
        self.comboBox.setItemText(0, _translate("MainWindow", "2024-2025"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2022-2023"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2023-2024"))
        self.pushButton_exit.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_logout.setText(_translate("MainWindow", "LOGOUT"))
