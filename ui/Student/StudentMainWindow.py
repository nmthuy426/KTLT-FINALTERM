# Form implementation generated from reading ui file 'D:\Documents\KTLT\FinalTerm\ui\Student\StudentMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 712)
        MainWindow.setMaximumSize(QtCore.QSize(1056, 752))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("backgound-color: rgba(0,0,0,0);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 712))
        self.label.setStyleSheet("QLabel:{\n"
"    border-radius: 20px;\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Documents\\KTLT\\FinalTerm\\ui\\Student\\../../image/55656.png"))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 860, 61))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(956, 16777215))
        self.label_2.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 90);\n"
"font-weight: bold;\n"
"font: 5000 18pt \"Arial\";\n"
"    border-top-left-radius: 25px;\n"
"    border-top-right-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-bottom-right-radius: 25px;\n"
"    padding: 10px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 580, 861, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Exit = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Exit.sizePolicy().hasHeightForWidth())
        self.pushButton_Exit.setSizePolicy(sizePolicy)
        self.pushButton_Exit.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_Exit.setMaximumSize(QtCore.QSize(1000, 60))
        self.pushButton_Exit.setSizeIncrement(QtCore.QSize(0, 500))
        self.pushButton_Exit.setStyleSheet("QPushButton {\n"
"    font: 5000 14pt \"Arial\"; /* Font Arial Black, size 12 */\n"
"    background-color: rgba(170,0,0,150); /* Màu nền đỏ đậm */\n"
"    color: rgb(255,255,255); /* Màu chữ trắng */\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    padding: 8px; /* Khoảng cách giữa chữ và viền */\n"
"    border: 4px solid rgba(255, 255,255, 200); /* Viền đỏ đậm */\n"
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
"}")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.horizontalLayout.addWidget(self.pushButton_Exit)
        self.pushButton_Logout = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Logout.sizePolicy().hasHeightForWidth())
        self.pushButton_Logout.setSizePolicy(sizePolicy)
        self.pushButton_Logout.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_Logout.setMaximumSize(QtCore.QSize(1000, 60))
        self.pushButton_Logout.setStyleSheet("QPushButton {\n"
"    font: 5000 14pt \"Arial\"; /* Font Arial Black, size 12 */\n"
"    background-color: rgba(255,255,255,100); /* Màu nền đỏ đậm */\n"
"    color: rgb(0,0,90); /* Màu chữ trắng */\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"    padding: 8px; /* Khoảng cách giữa chữ và viền */\n"
"    border: 4px solid rgba(255, 255,255, 200);\n"
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
"}")
        self.pushButton_Logout.setIconSize(QtCore.QSize(50, 20))
        self.pushButton_Logout.setObjectName("pushButton_Logout")
        self.horizontalLayout.addWidget(self.pushButton_Logout)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(70, 150, 861, 414))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(956, 1000))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("/* Tab chưa được chọn */\n"
"QTabBar::tab {\n"
"    width: 100px;\n"
"    min-height: 20px;\n"
"    text-align: center;\n"
"    padding:6px;\n"
"    color: #00005A;\n"
"    font: 2000 10pt \"Arial\";\n"
"    background: #EAEAEA;\n"
"}\n"
"\n"
"/* Tab được chọn */\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    color: #00008B;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* Tab cuối cùng có chiều dài lớn hơn */\n"
"QTabBar::tab:last {\n"
"    width: 250px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"/* Đặt nền trong suốt cho QTabWidget */\n"
"QTabWidget {\n"
"    background-color: rgba(0,0,0,0);\n"
"    border-bottom-left-radius: 12px;  \n"
"    border-bottom-right-radius: 12px;  \n"
"}\n"
"\n"
"/* Làm trong suốt nền của tab content */\n"
"QTabWidget::pane {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: none;\n"
"}\n"
"\n"
"/* Đảm bảo widget con cũng trong suốt */\n"
"\n"
"QTabBar::tab:last {\n"
"    width: 250px; /* Giới hạn chiều dài */\n"
"    text-align: center;\n"
"}\n"
"QTabBar::tab:middle {\n"
"    width: 250px; /* Giới hạn chiều dài */\n"
"    text-align: center;\n"
"}\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_score = QtWidgets.QWidget()
        self.tab_score.setObjectName("tab_score")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tab_score)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 861, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_grade = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_grade.sizePolicy().hasHeightForWidth())
        self.table_grade.setSizePolicy(sizePolicy)
        self.table_grade.setMinimumSize(QtCore.QSize(768, 0))
        self.table_grade.setMaximumSize(QtCore.QSize(900, 500))
        self.table_grade.setMouseTracking(False)
        self.table_grade.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.table_grade.setStyleSheet("/* Header trên cùng */\n"
"QHeaderView::section {\n"
"    background: rgb(255,255,255);  /* Màu xanh đậm */\n"
"    color: rgb(0,0,90);  /* Chữ trắng */\n"
"    font: 2000 12px \"Arial\";\n"
"}\n"
"QTableWidget:{\n"
"    background-color: rgb(255,255,255);\n"
"    color: rgb(255,255,255);  /* Chữ trắng */\n"
"    border: 1px solid rgb(0,0,90);  /* Viền trắng nhẹ */\n"
"    font: 1000 12px \"Arial\";\n"
"}\n"
"")
        self.table_grade.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.table_grade.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.table_grade.setAutoScrollMargin(16)
        self.table_grade.setColumnCount(6)
        self.table_grade.setObjectName("table_grade")
        self.table_grade.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        item.setFont(font)
        self.table_grade.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_grade.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_grade.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_grade.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_grade.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_grade.setHorizontalHeaderItem(5, item)
        self.table_grade.horizontalHeader().setCascadingSectionResizes(True)
        self.table_grade.horizontalHeader().setDefaultSectionSize(170)
        self.table_grade.horizontalHeader().setSortIndicatorShown(True)
        self.table_grade.horizontalHeader().setStretchLastSection(True)
        self.table_grade.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout.addWidget(self.table_grade)
        self.pushButton_updatescore = QtWidgets.QPushButton(parent=self.tab_score)
        self.pushButton_updatescore.setGeometry(QtCore.QRect(0, 332, 861, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_updatescore.sizePolicy().hasHeightForWidth())
        self.pushButton_updatescore.setSizePolicy(sizePolicy)
        self.pushButton_updatescore.setMinimumSize(QtCore.QSize(768, 50))
        self.pushButton_updatescore.setMaximumSize(QtCore.QSize(956, 40))
        self.pushButton_updatescore.setStyleSheet("QPushButton {\n"
"    font: 5000 14pt \"Arial\"; /* Font Arial Black, size 12 */\n"
"    background-color: rgba(0,85,0,100); /* Màu nền đỏ đậm */\n"
"    color: rgb(0, 85, 0); /* Màu chữ trắng */\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
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
        self.pushButton_updatescore.setObjectName("pushButton_updatescore")
        self.tabWidget.addTab(self.tab_score, "")
        self.tab_schedule = QtWidgets.QWidget()
        self.tab_schedule.setObjectName("tab_schedule")
        self.scrollArea_4 = QtWidgets.QScrollArea(parent=self.tab_schedule)
        self.scrollArea_4.setGeometry(QtCore.QRect(1, 0, 861, 381))
        self.scrollArea_4.setMinimumSize(QtCore.QSize(768, 0))
        self.scrollArea_4.setMaximumSize(QtCore.QSize(956, 16777215))
        self.scrollArea_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 859, 379))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 841, 361))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget_schedule = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget_3)
        self.tableWidget_schedule.setObjectName("tableWidget_schedule")
        self.tableWidget_schedule.setColumnCount(0)
        self.tableWidget_schedule.setRowCount(0)
        self.verticalLayout_5.addWidget(self.tableWidget_schedule)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.tabWidget.addTab(self.tab_schedule, "")
        self.tab_notice = QtWidgets.QWidget()
        self.tab_notice.setObjectName("tab_notice")
        self.scrollArea_5 = QtWidgets.QScrollArea(parent=self.tab_notice)
        self.scrollArea_5.setGeometry(QtCore.QRect(0, 0, 861, 381))
        self.scrollArea_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 859, 379))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_5)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 841, 361))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableWidget_registeclass = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget_5)
        self.tableWidget_registeclass.setObjectName("tableWidget_registeclass")
        self.tableWidget_registeclass.setColumnCount(0)
        self.tableWidget_registeclass.setRowCount(0)
        self.verticalLayout_7.addWidget(self.tableWidget_registeclass)
        self.pushButton_save = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy)
        self.pushButton_save.setMaximumSize(QtCore.QSize(1000, 40))
        self.pushButton_save.setStyleSheet("QPushButton {\n"
"    font: 5000 14pt \"Arial\"; /* Font Arial Black, size 12 */\n"
"    background-color: rgba(0,85,0,100); /* Màu nền đỏ đậm */\n"
"    color: rgb(0, 85, 0); /* Màu chữ trắng */\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    padding: 4px; /* Khoảng cách giữa chữ và viền */\n"
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
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout_7.addWidget(self.pushButton_save)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.tabWidget.addTab(self.tab_notice, "")
        self.tab_inforstudent = QtWidgets.QWidget()
        self.tab_inforstudent.setMinimumSize(QtCore.QSize(956, 0))
        self.tab_inforstudent.setMaximumSize(QtCore.QSize(768, 16777215))
        self.tab_inforstudent.setObjectName("tab_inforstudent")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.tab_inforstudent)
        self.scrollArea_2.setGeometry(QtCore.QRect(1, 0, 861, 381))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(956, 16777215))
        self.scrollArea_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 859, 379))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(140, 20, 251, 341))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_StuId = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_4)
        self.lineEdit_StuId.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_StuId.setSizeIncrement(QtCore.QSize(0, 10))
        self.lineEdit_StuId.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.lineEdit_StuId.setReadOnly(True)
        self.lineEdit_StuId.setObjectName("lineEdit_StuId")
        self.verticalLayout_6.addWidget(self.lineEdit_StuId)
        self.lineEdit_StuFullname = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_4)
        self.lineEdit_StuFullname.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_StuFullname.setSizeIncrement(QtCore.QSize(0, 10))
        self.lineEdit_StuFullname.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.lineEdit_StuFullname.setReadOnly(True)
        self.lineEdit_StuFullname.setObjectName("lineEdit_StuFullname")
        self.verticalLayout_6.addWidget(self.lineEdit_StuFullname)
        self.dateEdit_StuBir = QtWidgets.QDateEdit(parent=self.verticalLayoutWidget_4)
        self.dateEdit_StuBir.setMaximumSize(QtCore.QSize(16777215, 40))
        self.dateEdit_StuBir.setSizeIncrement(QtCore.QSize(0, 10))
        self.dateEdit_StuBir.setStyleSheet("QDateEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}\n"
"\n"
"QDateEdit::up-button {\n"
"    image: url(image/up-arrow.png);\n"
"    width: 10px;\n"
"    height: 12px;\n"
"    border: none;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right; /* Giữ vị trí */\n"
"    margin-right: 10px; /* Giảm khoảng cách */\n"
"    margin-top: 6px;\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"    image: url(image/down-arrow.png);\n"
"    width: 10px;\n"
"    height: 12px;\n"
"    border: none;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right; /* Giữ vị trí */\n"
"    margin-right: 10px; /* Giảm khoảng cách */\n"
"    margin-bottom: 6px;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    border: none;\n"
"} \n"
"")
        self.dateEdit_StuBir.setReadOnly(True)
        self.dateEdit_StuBir.setObjectName("dateEdit_StuBir")
        self.verticalLayout_6.addWidget(self.dateEdit_StuBir)
        self.comboBox_StuGender = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_4)
        self.comboBox_StuGender.setMaximumSize(QtCore.QSize(16777215, 40))
        self.comboBox_StuGender.setSizeIncrement(QtCore.QSize(0, 10))
        self.comboBox_StuGender.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo tròn cả 4 góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 30px; /* Chừa khoảng trống bên phải */\n"
"}\n"
"\n"
"/* Ẩn nền của nút dropdown để bo góc phải */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    background: transparent; /* Để nền trong suốt */\n"
"    width: 25px;\n"
"    subcontrol-position: right center;\n"
"}\n"
"\n"
"/* Tạo nền bo góc cho dropdown */\n"
"QComboBox::down-arrow {\n"
"    image: url(image/down-arrow.png);\n"
"    width: 10px;\n"
"    height: 12px;\n"
"    margin-right: 5px;\n"
"}\n"
"")
        self.comboBox_StuGender.setObjectName("comboBox_StuGender")
        self.comboBox_StuGender.addItem("")
        self.comboBox_StuGender.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox_StuGender)
        self.lineEdit_StuMail = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_4)
        self.lineEdit_StuMail.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_StuMail.setSizeIncrement(QtCore.QSize(0, 10))
        self.lineEdit_StuMail.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.lineEdit_StuMail.setReadOnly(True)
        self.lineEdit_StuMail.setObjectName("lineEdit_StuMail")
        self.verticalLayout_6.addWidget(self.lineEdit_StuMail)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 20, 111, 341))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_6.setStyleSheet("font: 1000 10pt \"Cambria\";\n"
"background-color: rgba(0,0,0,0);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_5.setStyleSheet("font: 1000 10pt \"Cambria\";\n"
"background-color: rgba(0,0,0,0);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_4.setStyleSheet("font: 1000 10pt \"Cambria\";\n"
"background-color: rgba(0,0,0,0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_7.setStyleSheet("font: 1000 10pt \"Cambria\";\n"
"background-color: rgba(0,0,0,0);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_8.setStyleSheet("font: 1000 10pt \"Cambria\";\n"
"background-color: rgba(0,0,0,0);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(570, 20, 271, 341))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LineEdit_StuCourse = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.LineEdit_StuCourse.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.LineEdit_StuCourse.setReadOnly(True)
        self.LineEdit_StuCourse.setObjectName("LineEdit_StuCourse")
        self.verticalLayout_3.addWidget(self.LineEdit_StuCourse)
        self.LineEdit_StuMajor = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.LineEdit_StuMajor.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.LineEdit_StuMajor.setReadOnly(True)
        self.LineEdit_StuMajor.setObjectName("LineEdit_StuMajor")
        self.verticalLayout_3.addWidget(self.LineEdit_StuMajor)
        self.LineEdit_StuClass = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.LineEdit_StuClass.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.LineEdit_StuClass.setReadOnly(True)
        self.LineEdit_StuClass.setObjectName("LineEdit_StuClass")
        self.verticalLayout_3.addWidget(self.LineEdit_StuClass)
        self.LineEdit_StuAdvisor = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.LineEdit_StuAdvisor.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.LineEdit_StuAdvisor.setReadOnly(True)
        self.LineEdit_StuAdvisor.setObjectName("LineEdit_StuAdvisor")
        self.verticalLayout_3.addWidget(self.LineEdit_StuAdvisor)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(410, 20, 147, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.khAHCLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.khAHCLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.khAHCLabel.setStyleSheet("font: 1000 10pt \"Cambria\";\n"
"background-color: rgba(0,0,0,0);")
        self.khAHCLabel.setObjectName("khAHCLabel")
        self.verticalLayout_4.addWidget(self.khAHCLabel)
        self.ngNhLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.ngNhLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ngNhLabel.setStyleSheet("font: 1000 10pt \"Cambria\";\n"
"background-color: rgba(0,0,0,0);")
        self.ngNhLabel.setObjectName("ngNhLabel")
        self.verticalLayout_4.addWidget(self.ngNhLabel)
        self.lPLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.lPLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lPLabel.setStyleSheet("font: 1000 10pt \"Cambria\";\n"
"background-color: rgba(0,0,0,0);")
        self.lPLabel.setObjectName("lPLabel")
        self.verticalLayout_4.addWidget(self.lPLabel)
        self.cVNHCTPLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.cVNHCTPLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.cVNHCTPLabel.setStyleSheet("font: 1000 10pt \"Cambria\";\n"
"background-color: rgba(0,0,0,0);")
        self.cVNHCTPLabel.setObjectName("cVNHCTPLabel")
        self.verticalLayout_4.addWidget(self.cVNHCTPLabel)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_inforstudent, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "STUDENT"))
        self.pushButton_Exit.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_Logout.setText(_translate("MainWindow", "LOGOUT"))
        item = self.table_grade.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SUBJECTS"))
        item = self.table_grade.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "FORMATIVE SCORE 1"))
        item = self.table_grade.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "FORMATIVE SCORE 2"))
        item = self.table_grade.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MIDTERM"))
        item = self.table_grade.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "FINALTERM"))
        item = self.table_grade.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "AVERAGE"))
        self.pushButton_updatescore.setText(_translate("MainWindow", "UPDATE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_score), _translate("MainWindow", "SCORE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_schedule), _translate("MainWindow", "SCHEDULE"))
        self.pushButton_save.setText(_translate("MainWindow", "SAVE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_notice), _translate("MainWindow", "REGISTER FOR CLASS"))
        self.comboBox_StuGender.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox_StuGender.setItemText(1, _translate("MainWindow", "Female"))
        self.label_6.setText(_translate("MainWindow", "Student ID:"))
        self.label_5.setText(_translate("MainWindow", "Full Name:"))
        self.label_4.setText(_translate("MainWindow", "Birthday:"))
        self.label_7.setText(_translate("MainWindow", "Gender:"))
        self.label_8.setText(_translate("MainWindow", "Email:"))
        self.khAHCLabel.setText(_translate("MainWindow", "Course:"))
        self.ngNhLabel.setText(_translate("MainWindow", "Major:"))
        self.lPLabel.setText(_translate("MainWindow", "Class:"))
        self.cVNHCTPLabel.setText(_translate("MainWindow", "Academic Advisor:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inforstudent), _translate("MainWindow", "PERSONAL INFORMATION"))
