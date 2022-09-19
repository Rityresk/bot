import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QColorDialog, QFontDialog
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QWidget, QDialog, QInputDialog
from PyQt5.QtGui import QColor, QPixmap, QFont
import sys
import sqlite3
from PIL import Image
import datetime as dt
from shutil import copy
from random import choice
import ctypes
import struct
import datetime
import win32com.client


class Ui_MainWindow_Redact_List(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 241)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(30, 90, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 90, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 26))
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
        self.add.setText(_translate("MainWindow", "Добавить картинку"))
        self.pushButton.setText(_translate("MainWindow", "Удалить картинку"))


class Ui_MainWindow_Maket(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(373, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 371, 410))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 410, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Удалить"))


class Ui_MainWindow_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 799)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 120, 180, 180))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 340, 351, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
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
        self.pushButton.setText(_translate("MainWindow", "Войти"))
        self.label_2.setText(_translate("MainWindow", "Логин"))
        self.label_3.setText(_translate("MainWindow", "Пароль"))
        self.pushButton_2.setText(_translate("MainWindow", "Зарегестрироваться"))
        self.label_4.setText(_translate("MainWindow", "Логин"))
        self.label_5.setText(_translate("MainWindow", "Пароль"))


class Ui_Dialog_User(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 230, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 70, 251, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 70, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 140, 251, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 55, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Логин"))
        self.label_2.setText(_translate("Dialog", "Пароль"))


class Ui_Dialog_Time(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 240, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 120, 191, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(232, 120, 151, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(426, 389)
        font = QtGui.QFont()
        font.setPointSize(9)
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 310, 201, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 256, 281))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setReadOnly(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 40, 141, 225))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "x"))
        self.label_2.setText(_translate("Dialog", "y"))
        self.label_3.setText(_translate("Dialog", "name"))
        self.label_4.setText(_translate("Dialog", "path"))


class Ui_MainWindow_Notes(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 799)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(25, 100, 861, 621))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 191, 31))
        self.label.setObjectName("label")
        self.poisk = QtWidgets.QLineEdit(self.centralwidget)
        self.poisk.setGeometry(QtCore.QRect(200, 40, 681, 22))
        self.poisk.setObjectName("poisk")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 29))
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
        self.label.setText(_translate("MainWindow", "Журнал заметок"))


class Ui_MainWindow_Options(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow1")
        MainWindow.resize(946, 799)
        self.centralwidget_1 = QtWidgets.QWidget(MainWindow)
        self.centralwidget_1.setObjectName("centralwidget")
        self.showava = QtWidgets.QLabel(self.centralwidget_1)
        self.showava.setGeometry(QtCore.QRect(44, 30, 120, 120))
        self.showava.setText("")
        self.showava.setObjectName("showava")
        self.showusername = QtWidgets.QLabel(self.centralwidget_1)
        self.showusername.setGeometry(QtCore.QRect(230, 70, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.showusername.setFont(font)
        self.showusername.setText("")
        self.showusername.setObjectName("showusername")
        self.changeava = QtWidgets.QPushButton(self.centralwidget_1)
        self.changeava.setGeometry(QtCore.QRect(139, 207, 251, 61))
        self.changeava.setObjectName("changeava")
        self.changelistpict = QtWidgets.QPushButton(self.centralwidget_1)
        self.changelistpict.setGeometry(QtCore.QRect(140, 320, 251, 61))
        self.changelistpict.setObjectName("changelistpict")
        self.changefont = QtWidgets.QPushButton(self.centralwidget_1)
        self.changefont.setGeometry(QtCore.QRect(140, 560, 251, 61))
        self.changefont.setObjectName("changefont")
        self.viewpict = QtWidgets.QPushButton(self.centralwidget_1)
        self.viewpict.setGeometry(QtCore.QRect(500, 320, 251, 61))
        self.viewpict.setObjectName("viewpict")
        self.changetime = QtWidgets.QPushButton(self.centralwidget_1)
        self.changetime.setGeometry(QtCore.QRect(140, 440, 251, 61))
        self.changetime.setObjectName("changetime")
        self.changecolor = QtWidgets.QPushButton(self.centralwidget_1)
        self.changecolor.setGeometry(QtCore.QRect(500, 440, 251, 61))
        self.changecolor.setObjectName("changecolor")
        self.changename = QtWidgets.QPushButton(self.centralwidget_1)
        self.changename.setGeometry(QtCore.QRect(500, 210, 251, 61))
        self.changename.setObjectName("changename")
        self.changeuser = QtWidgets.QPushButton(self.centralwidget_1)
        self.changeuser.setGeometry(QtCore.QRect(500, 560, 251, 61))
        self.changeuser.setObjectName("changeuser")
        MainWindow.setCentralWidget(self.centralwidget_1)
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 799)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 200, 181, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 320, 181, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 450, 181, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 200, 501, 334))
        self.label.setText("")
        self.label.setObjectName("label")
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
        self.pushButton.setText(_translate("MainWindow", "Оставить заметку"))
        self.pushButton_2.setText(_translate("MainWindow", "Настройки"))
        self.pushButton_3.setText(_translate("MainWindow", "Журнал заметок"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        newpath = r'C:\\main\\Pictures'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        er = open("note-color.txt", "r")
        r = er.read()
        er.close()
        if not r:
            r = rgb_to_hex((233, 233, 233))
        self.color = r
        self.dialogs = []
        global notes
        self.pushButton_2.clicked.connect(self.open_options)
        self.pushButton_3.clicked.connect(self.open_notes)
        self.pushButton.clicked.connect(self.make_note)
        con = sqlite3.connect("Notes.db")
        cur = con.cursor()
        wer = open("user_name.txt", "r").read()
        result = cur.execute("""SELECT * FROM Notes
                                WHERE user = ?""", (wer, )).fetchall()
        self.list = []
        f = open("note-font.txt", "r").read().split("+!")
        if f[-1] == "False":
            italic = False
        else:
            italic = True
        if f[-2] == "False":
            bold = False
        else:
            bold = True
        font = QFont(f[0], int(f[1]), italic=italic)
        font.setBold(bold)
        for elem in result:
            elem = list(elem)
            if elem[-1]:
                text = open(elem[0], 'r').read()
                t = Note_Form(int(elem[-3]), int(elem[-2]), text, elem[0], self.color)
                t.set_font(font)
                self.dialogs.append(t)
                self.list.append(t)
                notes.append(t)
                t.show()
        con.close()
        self.change()
        sa = open("cur.txt", "r").read()
        if not sa:
            sa = 'landscape-forest-trees-nature-2004265.jpg'
        b = 501
        c = 334
        img = Image.open(sa)
        img = img.resize((b, c), Image.ANTIALIAS)
        img.save('somepic.png')
        r = QPixmap("somepic.png")
        self.label.setPixmap(r)

    def open_options(self):
        global opt
        opt = Options()
        self.dialogs.append(opt)
        opt.show()

    def open_notes(self):
        note = Notes()
        self.dialogs.append(note)
        note.show()

    def make_note(self):
        dlg = Make_Note_Dialog()
        dlg.exec()
        s = dlg.ui
        x = s.lineEdit.text()
        y = s.lineEdit_2.text()
        name = s.lineEdit_3.text()
        text = s.textBrowser.toPlainText()
        path = s.lineEdit_4.text()
        if x != '' and y != '' and text != '' and name != '':
            if not path:
                path = name + ".txt"
            k = open(path, 'w+')
            k.write(text)
            k.close()
            t = open("user_name.txt", 'r').read()
            sqlite_connection = sqlite3.connect('Notes.db')
            cursor = sqlite_connection.cursor()
            sqlite_insert_query = """INSERT INTO Notes
                                     (path, date, user, x, y, show)
                                     VALUES
                                     (?, ?, ?, ?, ?, ?);"""
            count = cursor.execute(sqlite_insert_query, (path, dt.datetime.now().date(), t, x, y, True))
            sqlite_connection.commit()
            cursor.close()
            x = int(x)
            y = int(y)
            d = Note_Form(x, y, text, path, self.color)
            self.dialogs.append(d)
            d.show()

    def change(self):
        p = open("time.txt", 'r').read()
        i = p.split()
        k = i[0].split('-')
        t = i[1].split(':')
        yt = dt.datetime.now()
        global minutes
        if yt >= dt.datetime(int(k[0]), int(k[1]), int(k[2]), int(t[0]), int(t[0]), int(t[1]), round(float(t[2]))):
            global pict
            s = ''
            while not s:
                s = choice(pict)
            d = open("cur.txt", "w+")
            d.write(s)
            SPI_SETDESKWALLPAPER = 20
            is_64bit_windows = struct.calcsize('P') * 8 == 64
            if is_64bit_windows:
                ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, s, 3)
            else:
                ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, s, 3)
            scheduler = win32com.client.Dispatch('Schedule.Service')
            scheduler.Connect()
            root_folder = scheduler.GetFolder('\\')
            task_def = scheduler.NewTask(0)
            start_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
            TASK_TRIGGER_TIME = 1
            trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
            trigger.StartBoundary = start_time.isoformat()
            TASK_ACTION_EXEC = 0
            action = task_def.Actions.Create(TASK_ACTION_EXEC)
            action.ID = 'DO NOTHING'
            action.Path = "C:\\Python38\\python.exe"
            action.Arguments = 'Critt.py'
            action.WorkingDirectory = 'C:\\main'
            task_def.RegistrationInfo.Description = 'Test Task'
            task_def.Settings.Enabled = True
            task_def.Settings.StopIfGoingOnBatteries = False
            TASK_CREATE_OR_UPDATE = 6
            TASK_LOGON_NONE = 0
            root_folder.RegisterTaskDefinition(
                'Test Task',  # Task name
                task_def,
                TASK_CREATE_OR_UPDATE,
                '',  # No user
                '',  # No password
                TASK_LOGON_NONE)
            p = open("time.txt", 'w+')
            p.write(str(yt))


class Options(QMainWindow, Ui_MainWindow_Options):
    def __init__(self):
        super().__init__()
        self.dialogs = []
        self.setupUi(self)
        self.changename.clicked.connect(self.name)
        with open('avatar.txt', 'r') as file:
            path = file.read()
        if path == "":
            path = 'profile.png'
        img = Image.open(path)
        img = img.resize((120, 120), Image.ANTIALIAS)
        img.save('smallprof.png')
        r = QPixmap("smallprof.png")
        self.showava.setPixmap(r)
        with open('user_name.txt', 'r') as file:
            f = file.read()
        if f == "":
            f = 'User'
        self.showusername.setText(f)
        self.changeava.clicked.connect(self.avatar)
        self.changecolor.clicked.connect(self.color)
        self.changelistpict.clicked.connect(self.redact)
        self.changefont.clicked.connect(self.note_font)
        self.viewpict.clicked.connect(self.view)
        self.changetime.clicked.connect(self.choose_time)
        self.changeuser.clicked.connect(self.change_user)

    def name(self):
        h = Options_Dialog_Name()
        p = h.run()
        with open('user_name.txt', 'r') as file:
            filedata = file.read()
        old = filedata
        filedata = filedata.replace(filedata, p)
        with open('user_name.txt', 'w') as file:
            file.write(filedata)
        sqlite_connection = sqlite3.connect('Users.db')
        cursor = sqlite_connection.cursor()
        sql_update_query = """Update Users set user = ? where user = ?"""
        cursor.execute(sql_update_query, (p, old))
        sqlite_connection.commit()
        cursor.close()
        self.showusername.setText(p)

    def color(self):
        r = Color_Dialog()
        color = r.run()
        r = color.getRgb()
        t = list(r)
        r = rgb_to_hex((t[0], t[1], t[2]))
        w = open("note-color.txt", 'w+')
        w.write(r)
        global notes
        for i in notes:
            i.change_color(r)

    def avatar(self):
        h = Options_Dialog_Ava()
        path = h.run()
        if path:
            img = Image.open(path)
            img = img.resize((120, 120), Image.ANTIALIAS)
            img.save('smallprof.png')
            r = QPixmap("smallprof.png")
            self.showava.setPixmap(r)
            with open('avatar.txt', 'r') as file:
                filedata = file.read()
            old = filedata
            filedata = filedata.replace(filedata, path)
            with open('avatar.txt', 'w') as file:
                file.write(filedata)
            sqlite_connection = sqlite3.connect('Users.db')
            cursor = sqlite_connection.cursor()
            sql_update_query = """Update Users set ava = ? where ava = ?"""
            cursor.execute(sql_update_query, (path, old))
            sqlite_connection.commit()
            cursor.close()

    def redact(self):
        r = Choose()
        self.dialogs.append(r)
        r.show()

    def view(self):
        r = Del_Pict()
        p = r.slot_btn_chooseFile()

    def note_font(self):
        global notes
        f = Note_Font_Dialog()
        r = f.openFontDialog()
        if r:
            self.font = r[0]
            t = open("note-font.txt", "w+")
            r[2] = str(r[2])
            r[3] = str(r[3])
            r[4] = str(r[4])
            y = "+!".join(r[1:])
            e = t.write(y)
            for i in notes:
                i.set_font(self.font)

    def choose_time(self):
        global minutes
        dlg = Choose_Time_Dialog()
        dlg.exec()
        s = dlg.ui
        if s.lineEdit.text():
            t = int(s.lineEdit.text())
            f = s.comboBox.currentText()
            if f == 'часы':
                t *= 60
            minutes = t

    def change_user(self):
        dlg = Change_User_Dialog()
        dlg.exec()
        s = dlg.ui
        log = s.lineEdit.text()
        passw = s.lineEdit_2.text()
        con = sqlite3.connect("Users.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM Users
                                WHERE login = ? and password = ?""", (log, passw)).fetchall()
        if result:
            global main
            global notes
            global opt
            elem = result[0]
            main.close()
            opt.close()
            for i in notes:
                i.close()
            r = open("user_name.txt", "w+")
            r.write(elem[0])
            r.close()
            t = open("avatar.txt", "w+")
            t.write(elem[-1])
            t.close()
            main = MyWidget()
            self.dialogs.append(main)
            main.show()


class Notes(QMainWindow, Ui_MainWindow_Notes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.insertColumn(0)
        self.tableWidget.insertColumn(1)
        self.tableWidget.insertColumn(2)
        self.tableWidget.insertRow(0)
        self.tableWidget.setItem(0, 0, QTableWidgetItem('Text'))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Date"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("User"))
        con = sqlite3.connect("Notes.db")
        cur = con.cursor()
        user = open("user_name.txt", "r").read()
        result = cur.execute("""SELECT * FROM Notes
                                WHERE user = ?""", (user, )).fetchall()
        x = 1
        self.list = []
        for elem in result:
            elem = list(elem)
            text = open(elem[0], 'r').read()
            self.tableWidget.insertRow(x)
            self.tableWidget.setItem(x, 0, QTableWidgetItem(text))
            self.tableWidget.setItem(x, 1, QTableWidgetItem(elem[1]))
            self.tableWidget.setItem(x, 2, QTableWidgetItem(elem[2]))
            self.list.append([text, elem[1], elem[2]])
            x += 1
        con.close()
        self.poisk.textChanged.connect(self.search)

    def search(self):
        if len(self.poisk.text()) >= 3:
            for i in range(1, self.tableWidget.rowCount()):
                self.tableWidget.removeRow(1)
            x = 1
            for i in self.list:
                if self.poisk.text().lower() in i[0].lower():
                    self.tableWidget.insertRow(x)
                    for j in range(3):
                        self.tableWidget.setItem(x, j, QTableWidgetItem(i[j]))
                        self.tableWidget.item(x, j)
                    x += 1
        if len(self.poisk.text()) == 0:
            x = 1
            for elem in self.list:
                self.tableWidget.insertRow(x)
                self.tableWidget.setItem(x, 0, QTableWidgetItem(elem[0]))
                self.tableWidget.setItem(x, 1, QTableWidgetItem(elem[1]))
                self.tableWidget.setItem(x, 2, QTableWidgetItem(elem[2]))
                x += 1


class Options_Dialog_Name(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Диалоговые окна')

    def run(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                "Как тебя зовут?")
        if ok_pressed:
            return name


class Options_Dialog_Ava(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Диалоговые окна')

    def run(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '',
                                            'Картинка (*.png);;Картинка (*.jpg);;Все файлы (*)')[0]
        return fname


class Make_Note_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class Change_User_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_User()
        self.ui.setupUi(self)


class Choose_Time_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_Time()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem('минуты')
        self.ui.comboBox.addItem('часы')


class Note_Form(QMainWindow, Ui_MainWindow_Maket):
    def __init__(self, x, y, text, path, color):
        super().__init__()
        self.color = color
        self.setupUi(self)
        self.move(x, y)
        self.textBrowser.setText(text)
        self.textBrowser.setStyleSheet("background-color: {}".format(color))
        self.path = path
        self.pushButton.setStyleSheet("background-color: {}".format(color))
        self.pushButton.clicked.connect(self.set_show_False)

    def change_color(self, color):
        self.textBrowser.setStyleSheet("background-color: {}".format(color))
        self.pushButton.setStyleSheet("background-color: {}".format(color))

    def set_show_False(self):
        self.close()
        con = sqlite3.connect("Notes.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM Notes
                                WHERE user = User""").fetchall()
        result = con.execute("""UPDATE Notes SET show = ? Where path = ?""", (False, self.path))
        con.commit()
        cur.close()

    def set_font(self, font):
        self.textBrowser.setFont(font)


class Color_Dialog(QWidget):
    def __init__(self):
        super().__init__()

    def run(self):
        color = QColorDialog.getColor()
        if color.isValid():
            return color


class Note_Font_Dialog(QWidget):
    def __init__(self):
        super().__init__()

    def openFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            return [font, font.family(), font.pointSize(), font.bold(), font.italic()]


class Choose(QMainWindow, Ui_MainWindow_Redact_List):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add.clicked.connect(self.plus)
        self.pushButton.clicked.connect(self.delete)

    def plus(self):
        h = Options_Dialog_Ava()
        path = h.run()
        e = path.split("/")[-1]
        t = f'C:\\main\\Pictures\\{e}'
        copy(path, t)
        r = open("list_of_pict.txt", 'r').read()
        u = open("list_of_pict.txt", 'w')
        u.write(f'{r}\n{t}\n')

    def delete(self):
        h = Del_Pict()
        path = h.slot_btn_chooseFile()
        if path:
            with open('list_of_pict.txt', 'r') as file:
                filedata = file.read()
            filedata = filedata.replace(path, '')
            with open('list_of_pict.txt', 'w') as file:
                file.write(filedata)
            os.remove(path)


class Login(QMainWindow, Ui_MainWindow_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        img = Image.open('profile.png')
        img = img.resize((180, 180), Image.ANTIALIAS)
        img.save('login.png')
        r = QPixmap("login.png")
        self.dialogs = []
        self.label.setPixmap(r)
        self.pushButton.clicked.connect(self.old)
        self.pushButton_2.clicked.connect(self.new)

    def new(self):
        sqlite_connection = sqlite3.connect('Users.db')
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = """INSERT INTO Users
                                (user, login, password, ava)
                                VALUES
                                (?, ?, ?, ?);"""
        count = cursor.execute(sqlite_insert_query, ("User", self.lineEdit_3.text(),
                                                     self.lineEdit_4.text(), "profile.png"))
        sqlite_connection.commit()
        cursor.close()
        main = MyWidget()
        p = open('user_name.txt', "w+")
        p.write("User")
        wq = open("avatar.txt", "w+")
        wq.write('profile.png')
        self.dialogs.append(main)
        main.show()
        self.close()

    def old(self):
        global main
        log = self.lineEdit.text()
        passw = self.lineEdit_2.text()
        con = sqlite3.connect("Users.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM Users
                                WHERE login = ? and password = ?""", (log, passw)).fetchall()
        if result:
            for elem in result:
                p = open("user_name.txt", 'w+')
                p.write(elem[0])
                p.close()
                i = open('avatar.txt', "w+")
                i.write(elem[-1])
                i.close()
                main = MyWidget()
                self.dialogs.append(main)
                main.show()
                self.close()


class Del_Pict(QWidget):
    def __init__(self):
        super().__init__()
        self.cwd = "C:\\main\\Pictures"
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Диалоговые окна')

    def slot_btn_chooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, "Выбрать файл", self.cwd,
                                                                'Все файлы (*)')
        return fileName_choose


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


notes = []
pict = open("list_of_pict.txt", "r").read().split("\n")
minutes = open("minutes.txt", 'r').read()
if minutes:
    minutes = int(minutes)
else:
    minutes = 60
user = open('user_name.txt', 'r').read()
if not user:
    user = "User"
main = ''
opt = ''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec_())