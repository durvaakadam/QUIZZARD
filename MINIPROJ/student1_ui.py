# Form implementation generated from reading ui file 'c:\Users\durva\Downloads\mini4 (2)\mini4\student1.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1292, 690)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 110, 591, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("color: rgb(85, 255, 255);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\durva\\Downloads\\mini4 (2)\\mini4\\../../quizzard-high-resolution-logo-black-transparent.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1291, 691))
        self.label.setStyleSheet("background-color:rgb(99,34,64);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\durva\\Downloads\\mini4 (2)\\mini4\\../../244.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 460, 211, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(252, 196, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 137, 143, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"    font: 63 17pt \"Segoe UI Variable Display Semib\";\n"
"border-radius:20px;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(188, 188, 188);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 470, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "     GET STARTED"))
        self.label_3.setText(_translate("MainWindow", ">"))