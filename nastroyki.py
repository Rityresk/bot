# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nastroyki.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 799)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.showava = QtWidgets.QLabel(self.centralwidget)
        self.showava.setGeometry(QtCore.QRect(44, 30, 121, 101))
        self.showava.setText("")
        self.showava.setObjectName("showava")
        self.showusername = QtWidgets.QLabel(self.centralwidget)
        self.showusername.setGeometry(QtCore.QRect(230, 70, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.showusername.setFont(font)
        self.showusername.setText("")
        self.showusername.setObjectName("showusername")
        self.changeava = QtWidgets.QPushButton(self.centralwidget)
        self.changeava.setGeometry(QtCore.QRect(139, 207, 251, 61))
        self.changeava.setObjectName("changeava")
        self.changelistpict = QtWidgets.QPushButton(self.centralwidget)
        self.changelistpict.setGeometry(QtCore.QRect(140, 320, 251, 61))
        self.changelistpict.setObjectName("changelistpict")
        self.changefont = QtWidgets.QPushButton(self.centralwidget)
        self.changefont.setGeometry(QtCore.QRect(140, 560, 251, 61))
        self.changefont.setObjectName("changefont")
        self.viewpict = QtWidgets.QPushButton(self.centralwidget)
        self.viewpict.setGeometry(QtCore.QRect(500, 320, 251, 61))
        self.viewpict.setObjectName("viewpict")
        self.changetime = QtWidgets.QPushButton(self.centralwidget)
        self.changetime.setGeometry(QtCore.QRect(140, 440, 251, 61))
        self.changetime.setObjectName("changetime")
        self.changecolor = QtWidgets.QPushButton(self.centralwidget)
        self.changecolor.setGeometry(QtCore.QRect(500, 440, 251, 61))
        self.changecolor.setObjectName("changecolor")
        self.changename = QtWidgets.QPushButton(self.centralwidget)
        self.changename.setGeometry(QtCore.QRect(500, 210, 251, 61))
        self.changename.setObjectName("changename")
        self.changeuser = QtWidgets.QPushButton(self.centralwidget)
        self.changeuser.setGeometry(QtCore.QRect(500, 560, 251, 61))
        self.changeuser.setObjectName("changeuser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.changeava.setText(_translate("MainWindow", "Сменить аватар пользователя"))
        self.changelistpict.setText(_translate("MainWindow", "Редактировать список картинок"))
        self.changefont.setText(_translate("MainWindow", "Сменить шрифт заметок по умолчанию"))
        self.viewpict.setText(_translate("MainWindow", "Посмотреть картинки"))
        self.changetime.setText(_translate("MainWindow", "Сменить частоту обновления"))
        self.changecolor.setText(_translate("MainWindow", "Сменить цвет заметок по умолчанию"))
        self.changename.setText(_translate("MainWindow", "Сменить имя пользователя"))
        self.changeuser.setText(_translate("MainWindow", "Сменить пользователя"))
