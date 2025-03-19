# Form implementation generated from reading ui file 'D:\Documents\KTLT\FinalTerm\ui\Admin\AdminMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdminManagement(object):
    def setupUi(self, AdminManagement):
        AdminManagement.setObjectName("AdminManagement")
        AdminManagement.resize(1000, 712)
        AdminManagement.setStyleSheet("QPushButton {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=AdminManagement)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 712))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Documents\\KTLT\\FinalTerm\\ui\\Admin\\../../image/Purple and White Modern Login and Sign-up Website Page UI Desktop Prototype (1000 x 710 px) (1000 x 710 px) (1000 x 712 px)1111.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1000, 712))
        self.tabWidget.setStyleSheet("/* Tab chưa được chọn */\n"
"QTabBar::tab {\n"
"    width: 100px;\n"
"    height: 30px;\n"
"    min-height: 20px;\n"
"    text-align: center;\n"
"    color: #00005A;\n"
"    font: 2000 10pt \"Arial\";\n"
"    padding: 6px 12px;\n"
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
"QTabBar::tab {\n"
"    width: 300px;\n"
"    text-align: center;\n"
"}\n"
"QTabBar::tab:middle {\n"
"    width: 328px;\n"
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
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_ManageAccounts = QtWidgets.QWidget()
        self.tab_ManageAccounts.setObjectName("tab_ManageAccounts")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tab_ManageAccounts)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 981, 641))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_InfoTeacher = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget)
        self.groupBox_InfoTeacher.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_InfoTeacher.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox_InfoTeacher.setStyleSheet("font: 2000 12pt \"Arial\";\n"
"color: rgb(0,0,90);")
        self.groupBox_InfoTeacher.setObjectName("groupBox_InfoTeacher")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.groupBox_InfoTeacher)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(140, 30, 351, 261))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit_TeaId = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_TeaId.sizePolicy().hasHeightForWidth())
        self.lineEdit_TeaId.setSizePolicy(sizePolicy)
        self.lineEdit_TeaId.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit_TeaId.setSizeIncrement(QtCore.QSize(0, 10))
        self.lineEdit_TeaId.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.lineEdit_TeaId.setObjectName("lineEdit_TeaId")
        self.verticalLayout_7.addWidget(self.lineEdit_TeaId)
        self.lineEdit_TeaFullname = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_TeaFullname.sizePolicy().hasHeightForWidth())
        self.lineEdit_TeaFullname.setSizePolicy(sizePolicy)
        self.lineEdit_TeaFullname.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit_TeaFullname.setSizeIncrement(QtCore.QSize(0, 10))
        self.lineEdit_TeaFullname.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.lineEdit_TeaFullname.setObjectName("lineEdit_TeaFullname")
        self.verticalLayout_7.addWidget(self.lineEdit_TeaFullname)
        self.dateEdit_TeaBir = QtWidgets.QDateEdit(parent=self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_TeaBir.sizePolicy().hasHeightForWidth())
        self.dateEdit_TeaBir.setSizePolicy(sizePolicy)
        self.dateEdit_TeaBir.setMaximumSize(QtCore.QSize(16777215, 50))
        self.dateEdit_TeaBir.setSizeIncrement(QtCore.QSize(0, 10))
        self.dateEdit_TeaBir.setStyleSheet("QDateEdit {\n"
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
        self.dateEdit_TeaBir.setObjectName("dateEdit_TeaBir")
        self.verticalLayout_7.addWidget(self.dateEdit_TeaBir)
        self.comboBox_TeaGender = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_TeaGender.sizePolicy().hasHeightForWidth())
        self.comboBox_TeaGender.setSizePolicy(sizePolicy)
        self.comboBox_TeaGender.setMaximumSize(QtCore.QSize(16777215, 50))
        self.comboBox_TeaGender.setSizeIncrement(QtCore.QSize(0, 10))
        self.comboBox_TeaGender.setStyleSheet("QComboBox {\n"
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
        self.comboBox_TeaGender.setObjectName("comboBox_TeaGender")
        self.comboBox_TeaGender.addItem("")
        self.comboBox_TeaGender.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_TeaGender)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(parent=self.groupBox_InfoTeacher)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 30, 121, 261))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_7)
        self.label_8.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_7)
        self.label_9.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_7)
        self.label_10.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_7)
        self.label_11.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(parent=self.groupBox_InfoTeacher)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(510, 30, 81, 191))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(7)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_18 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_10)
        self.label_18.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_12.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_10)
        self.label_19.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_12.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_10)
        self.label_20.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_12.addWidget(self.label_20)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(parent=self.groupBox_InfoTeacher)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(600, 30, 371, 261))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lineEdit_TeaMail = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_TeaMail.sizePolicy().hasHeightForWidth())
        self.lineEdit_TeaMail.setSizePolicy(sizePolicy)
        self.lineEdit_TeaMail.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit_TeaMail.setSizeIncrement(QtCore.QSize(0, 10))
        self.lineEdit_TeaMail.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.lineEdit_TeaMail.setObjectName("lineEdit_TeaMail")
        self.verticalLayout_13.addWidget(self.lineEdit_TeaMail)
        self.lineEdit_TeaFaculty = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_TeaFaculty.sizePolicy().hasHeightForWidth())
        self.lineEdit_TeaFaculty.setSizePolicy(sizePolicy)
        self.lineEdit_TeaFaculty.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit_TeaFaculty.setSizeIncrement(QtCore.QSize(0, 10))
        self.lineEdit_TeaFaculty.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.lineEdit_TeaFaculty.setObjectName("lineEdit_TeaFaculty")
        self.verticalLayout_13.addWidget(self.lineEdit_TeaFaculty)
        self.lineEdit_TeaClass = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_TeaClass.sizePolicy().hasHeightForWidth())
        self.lineEdit_TeaClass.setSizePolicy(sizePolicy)
        self.lineEdit_TeaClass.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lineEdit_TeaClass.setSizeIncrement(QtCore.QSize(0, 10))
        self.lineEdit_TeaClass.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.lineEdit_TeaClass.setObjectName("lineEdit_TeaClass")
        self.verticalLayout_13.addWidget(self.lineEdit_TeaClass)
        self.pushButton_TeaAddInfo = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_11)
        self.pushButton_TeaAddInfo.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_TeaAddInfo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_TeaAddInfo.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(0,0,90);\n"
"font: 2000 12pt \"Arial\";")
        self.pushButton_TeaAddInfo.setObjectName("pushButton_TeaAddInfo")
        self.verticalLayout_13.addWidget(self.pushButton_TeaAddInfo)
        self.verticalLayout.addWidget(self.groupBox_InfoTeacher)
        self.groupBox_InfoStudent = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget)
        self.groupBox_InfoStudent.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox_InfoStudent.setMaximumSize(QtCore.QSize(16777215, 500))
        self.groupBox_InfoStudent.setStyleSheet("font: 2000 12pt \"Arial\";\n"
"color: rgb(0,0,90);")
        self.groupBox_InfoStudent.setObjectName("groupBox_InfoStudent")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_InfoStudent)
        self.formLayoutWidget.setGeometry(QtCore.QRect(490, 40, 151, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.khAHCLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.khAHCLabel.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.khAHCLabel.setObjectName("khAHCLabel")
        self.verticalLayout_4.addWidget(self.khAHCLabel)
        self.ngNhLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.ngNhLabel.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.ngNhLabel.setObjectName("ngNhLabel")
        self.verticalLayout_4.addWidget(self.ngNhLabel)
        self.lPLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.lPLabel.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.lPLabel.setObjectName("lPLabel")
        self.verticalLayout_4.addWidget(self.lPLabel)
        self.cVNHCTPLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.cVNHCTPLabel.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.cVNHCTPLabel.setObjectName("cVNHCTPLabel")
        self.verticalLayout_4.addWidget(self.cVNHCTPLabel)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.groupBox_InfoStudent)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(140, 40, 331, 271))
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
        self.lineEdit_StuMail.setObjectName("lineEdit_StuMail")
        self.verticalLayout_6.addWidget(self.lineEdit_StuMail)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=self.groupBox_InfoStudent)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 40, 121, 271))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_6.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_5.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_4.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_7.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_3.setStyleSheet("font: 1000 10pt \"Cambria\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.groupBox_InfoStudent)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(650, 40, 322, 281))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LineEdit_StuCourse = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_3)
        self.LineEdit_StuCourse.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.LineEdit_StuCourse.setObjectName("LineEdit_StuCourse")
        self.verticalLayout_3.addWidget(self.LineEdit_StuCourse)
        self.comboBox_StuMajor = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_3)
        self.comboBox_StuMajor.setMaximumSize(QtCore.QSize(16777215, 40))
        self.comboBox_StuMajor.setSizeIncrement(QtCore.QSize(0, 10))
        self.comboBox_StuMajor.setStyleSheet("QComboBox {\n"
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
        self.comboBox_StuMajor.setObjectName("comboBox_StuMajor")
        self.comboBox_StuMajor.addItem("")
        self.comboBox_StuMajor.addItem("")
        self.comboBox_StuMajor.addItem("")
        self.comboBox_StuMajor.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_StuMajor)
        self.comboBox_StuClass = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_3)
        self.comboBox_StuClass.setMaximumSize(QtCore.QSize(16777215, 40))
        self.comboBox_StuClass.setSizeIncrement(QtCore.QSize(0, 10))
        self.comboBox_StuClass.setStyleSheet("QComboBox {\n"
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
        self.comboBox_StuClass.setObjectName("comboBox_StuClass")
        self.verticalLayout_3.addWidget(self.comboBox_StuClass)
        self.LineEdit_StuAdvisor = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_3)
        self.LineEdit_StuAdvisor.setStyleSheet("QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 10px;\n"
"    font: 500 15px \"Cambria\";\n"
"    background: white;\n"
"    padding-right: 20px; /* Chừa khoảng trống bên phải */\n"
"}")
        self.LineEdit_StuAdvisor.setObjectName("LineEdit_StuAdvisor")
        self.verticalLayout_3.addWidget(self.LineEdit_StuAdvisor)
        self.pushButton_StuAddInfo = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButton_StuAddInfo.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_StuAddInfo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_StuAddInfo.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(0,0,90);\n"
"font: 2000 12pt \"Arial\";")
        self.pushButton_StuAddInfo.setObjectName("pushButton_StuAddInfo")
        self.verticalLayout_3.addWidget(self.pushButton_StuAddInfo)
        self.verticalLayout.addWidget(self.groupBox_InfoStudent)
        self.tabWidget.addTab(self.tab_ManageAccounts, "")
        self.tab_ListAccounts = QtWidgets.QWidget()
        self.tab_ListAccounts.setObjectName("tab_ListAccounts")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(parent=self.tab_ListAccounts)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 10, 981, 651))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget_8)
        self.groupBox_3.setStyleSheet("font: 2000 12pt \"Arial\";\n"
"color: rgb(0,0,90);")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableWidget_Student = QtWidgets.QTableWidget(parent=self.groupBox_3)
        self.tableWidget_Student.setGeometry(QtCore.QRect(10, 30, 961, 281))
        self.tableWidget_Student.setStyleSheet("QTableWidget {\n"
"    border-radius: 25px; /* Bo góc cả 4 góc */\n"
"    background: white;\n"
"}\n"
"")
        self.tableWidget_Student.setObjectName("tableWidget_Student")
        self.tableWidget_Student.setColumnCount(0)
        self.tableWidget_Student.setRowCount(0)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget_8)
        self.groupBox_4.setStyleSheet("font: 2000 12pt \"Arial\";\n"
"color: rgb(0,0,90);")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.tableWidget_Teacher = QtWidgets.QTableWidget(parent=self.groupBox_4)
        self.tableWidget_Teacher.setGeometry(QtCore.QRect(10, 30, 961, 281))
        self.tableWidget_Teacher.setStyleSheet("QTableWidget {\n"
"    border-radius: 25px; /* Bo góc cả 4 góc */\n"
"    background: white;\n"
"}\n"
"")
        self.tableWidget_Teacher.setObjectName("tableWidget_Teacher")
        self.tableWidget_Teacher.setColumnCount(0)
        self.tableWidget_Teacher.setRowCount(0)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tab_ListAccounts, "")
        self.tab_ManageClasses = QtWidgets.QWidget()
        self.tab_ManageClasses.setObjectName("tab_ManageClasses")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_ManageClasses)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 981, 651))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_Classes = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget_2)
        self.tableWidget_Classes.setMinimumSize(QtCore.QSize(0, 560))
        self.tableWidget_Classes.setMaximumSize(QtCore.QSize(16777215, 580))
        self.tableWidget_Classes.setStyleSheet("QTableWidget {\n"
"    border-radius: 25px; /* Bo góc cả 4 góc */\n"
"    background: white;\n"
"}\n"
"")
        self.tableWidget_Classes.setObjectName("tableWidget_Classes")
        self.tableWidget_Classes.setColumnCount(0)
        self.tableWidget_Classes.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget_Classes)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_CreateClass = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushButton_CreateClass.setStyleSheet("QPushButton {\n"
"    font: 5000 14pt \"Arial\"; /* Font Arial Black, size 12 */\n"
"    background-color: rgba(255,255,255,100); /* Màu nền đỏ đậm */\n"
"    color: rgb(0,0,90); /* Màu chữ trắng */\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-top-right-radius: 25px;\n"
"    border-bottom-right-radius: 25px;\n"
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
        self.pushButton_CreateClass.setObjectName("pushButton_CreateClass")
        self.horizontalLayout_2.addWidget(self.pushButton_CreateClass)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_ManageClasses, "")
        AdminManagement.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminManagement)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminManagement)

    def retranslateUi(self, AdminManagement):
        _translate = QtCore.QCoreApplication.translate
        AdminManagement.setWindowTitle(_translate("AdminManagement", "Admin Management"))
        self.groupBox_InfoTeacher.setTitle(_translate("AdminManagement", "TEACHER"))
        self.comboBox_TeaGender.setItemText(0, _translate("AdminManagement", "Male"))
        self.comboBox_TeaGender.setItemText(1, _translate("AdminManagement", "Female"))
        self.label_8.setText(_translate("AdminManagement", "Teacher ID:"))
        self.label_9.setText(_translate("AdminManagement", "Full Name:"))
        self.label_10.setText(_translate("AdminManagement", "Birthday:"))
        self.label_11.setText(_translate("AdminManagement", "Gender:"))
        self.label_18.setText(_translate("AdminManagement", "Email:"))
        self.label_19.setText(_translate("AdminManagement", "Faculty:"))
        self.label_20.setText(_translate("AdminManagement", "Class:"))
        self.pushButton_TeaAddInfo.setText(_translate("AdminManagement", "ADD TEACHER"))
        self.groupBox_InfoStudent.setTitle(_translate("AdminManagement", "STUDENT"))
        self.khAHCLabel.setText(_translate("AdminManagement", "Course:"))
        self.ngNhLabel.setText(_translate("AdminManagement", "Major:"))
        self.lPLabel.setText(_translate("AdminManagement", "Class:"))
        self.cVNHCTPLabel.setText(_translate("AdminManagement", "Academic Advisor:"))
        self.comboBox_StuGender.setItemText(0, _translate("AdminManagement", "Male"))
        self.comboBox_StuGender.setItemText(1, _translate("AdminManagement", "Female"))
        self.label_6.setText(_translate("AdminManagement", "Student ID:"))
        self.label_5.setText(_translate("AdminManagement", "Full Name:"))
        self.label_4.setText(_translate("AdminManagement", "Birthday:"))
        self.label_7.setText(_translate("AdminManagement", "Gender:"))
        self.label_3.setText(_translate("AdminManagement", "Email:"))
        self.comboBox_StuMajor.setItemText(0, _translate("AdminManagement", "Thương Mại Điện Tử"))
        self.comboBox_StuMajor.setItemText(1, _translate("AdminManagement", "Thương Mại Điện Tử (tiếng anh)"))
        self.comboBox_StuMajor.setItemText(2, _translate("AdminManagement", "Hệ Thống Thông Tin Quản Lý"))
        self.comboBox_StuMajor.setItemText(3, _translate("AdminManagement", "Kinh Doanh Số và Trí Tuệ Nhân Tạo"))
        self.pushButton_StuAddInfo.setText(_translate("AdminManagement", "ADD STUDENT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ManageAccounts), _translate("AdminManagement", "CREATE ACCOUNTS"))
        self.groupBox_3.setTitle(_translate("AdminManagement", "STUDENT"))
        self.groupBox_4.setTitle(_translate("AdminManagement", "TEACHER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ListAccounts), _translate("AdminManagement", "LISTS OF ACCOUNTS"))
        self.pushButton_CreateClass.setText(_translate("AdminManagement", "CREATE CLASS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ManageClasses), _translate("AdminManagement", "MANAGE CLASSES"))
