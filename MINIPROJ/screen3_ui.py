# Form implementation generated from reading ui file 'c:\Users\durva\Downloads\mini4 (2)\mini4\screen3.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1557, 1326)
        MainWindow.setStyleSheet("background-color: rgb(99,34,64);")
        self.widget = QtWidgets.QWidget(parent=MainWindow)
        self.widget.setStyleSheet("background-color: rgb(99,34,64);\n"
"border-radius:20px;")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(420, 260, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius:5px;\n"
"padding-left:10px;\n"
"border:1.5px solid rgba(0,0,0);\n"
"border-color: rgb(99, 34, 64);\n"
"padding-bottom:3px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 330, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0,0,0);\n"
"border-radius:5px;\n"
"padding-left:10px;\n"
"border:1.5px solid rgba(0,0,0);\n"
"border-color: rgb(99, 34, 64);\n"
"padding-bottom:3px")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.loginbutton = QtWidgets.QPushButton(parent=self.widget)
        self.loginbutton.setGeometry(QtCore.QRect(470, 420, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet("QPushButton{\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(72, 48, 80);\n"
"    color:rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(209, 199, 199);\n"
"}\n"
"")
        self.loginbutton.setObjectName("loginbutton")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(330, 120, 671, 401))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 5px solid black; ")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(490, 170, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(400, 150, 61, 81))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setPixmap(QtGui.QPixmap("c:\\Users\\durva\\Downloads\\mini4 (2)\\mini4\\../../lock.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(720, 150, 231, 301))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("c:\\Users\\durva\\Downloads\\mini4 (2)\\mini4\\../../tp1.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(120, 70, 121, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"font: 63 17pt \"Segoe UI Variable Small Semibol\";\n"
"border-radius: 25px;\n"
"color:black;\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"background-color: rgb(209, 199, 199);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1381, 781))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\durva\\Downloads\\mini4 (2)\\mini4\\../../WhatsApp Image 2024-03-22 at 2.43.00 AM.jpeg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.loginbutton.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.loginbutton.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Student Login"))
        self.pushButton.setText(_translate("MainWindow", "BACK"))
