from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QUrl
from data import db_session
from data.prjct import Place
import requests
from flask import Flask, render_template, redirect, request
import os
from data.rest import api as ai
from requests import get, post, delete
import flask
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify

app1 = Flask(__name__)


class Ren(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 240, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 81, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 139, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 150, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Номер 1"))
        self.label_2.setText(_translate("Dialog", "Номер 2"))


class Dl(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 240, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 81, 191, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Номер"))


class Viv(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 787)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 741, 61))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 120, 611, 471))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 650, 231, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 650, 231, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Предыдущий"))
        self.pushButton_2.setText(_translate("MainWindow", "Следующий"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 787)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 30, 141, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 100, 281, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 240, 351, 371))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 190, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 521, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 26))
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
        self.label.setText(_translate("MainWindow", "Мой список"))
        self.pushButton.setText(_translate("MainWindow", "Добавить место"))
        self.label_3.setText(_translate("MainWindow", "Любимое место"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 366)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 300, 191, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 301, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setReadOnly(False)
        self.label.setText(_translate("Dialog", "Адрес"))
        self.label_2.setText(_translate("Dialog", "Место в списке"))
        self.label_3.setText(_translate("Dialog", "Заметки"))


class Ui_List(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 787)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 20, 241, 61))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 38))
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
        self.label.setText(_translate("MainWindow", "Просмотр списков"))


class Ui_Menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 787)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 255, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 331, 591))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 120, 541, 511))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 26))
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
        self.pushButton_2.setText(_translate("MainWindow", "Просмотр чужих списков"))
        self.pushButton.setText(_translate("MainWindow", "Мой список"))
        self.pushButton_3.setText(_translate("MainWindow", "Показ карт из списка"))
        self.pushButton_4.setText(_translate("MainWindow", "Поменять местами"))
        self.pushButton_5.setText(_translate("MainWindow", "Удалить"))


class Main(QMainWindow, Ui_Menu):
    def __init__(self):
        super().__init__()
        self.dialogs = []
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ref)
        self.pushButton_2.clicked.connect(self.li)
        self.pushButton_3.clicked.connect(self.sh)
        self.pushButton_4.clicked.connect(self.ren)
        self.pushButton_5.clicked.connect(self.de)
        db_session.global_init("db/project.db")
        db_sess = db_session.create_session()
        k = db_sess.query(Place).first()
        t = k.coords.split()
        p = k.address
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={p}&format=json"
        response = requests.get(geocoder_request)
        if response:
            json_response = response.json()
            add = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['metaDataProperty'][
                'GeocoderMetaData']['text']
        api_server = "http://static-maps.yandex.ru/1.x/"
        lon = t[0]
        lat = t[1]
        spn = '0.005'
        params = {"ll": ",".join([lon, lat]),
                  "spn": ",".join([spn, spn]),
                  "l": "map"
                  }
        response = requests.get(api_server, params=params)
        map_file = "menu.jpg"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.initUI("menu.jpg")

    def de(self):
        dlg = D()
        dlg.exec()
        s = dlg.ui
        n = s.lineEdit.text()
        if n:
            n = int(n)
            db_session.global_init("db/project.db")
            db_sess = db_session.create_session()
            a = []
            for i in db_sess.query(Place).all():
                if i.id == n:
                    db_sess.delete(i)
                    db_sess.commit()

    def initUI(self, a):
        self.pixmap = QPixmap(a)
        self.label.setPixmap(self.pixmap)

    def ren(self):
        dlg = R()
        dlg.exec()
        s = dlg.ui
        n = s.lineEdit.text()
        r = s.lineEdit_2.text()
        if n and r:
            n = int(n)
            r = int(r)
            db_session.global_init("db/project.db")
            db_sess = db_session.create_session()
            a = []
            for i in db_sess.query(Place).all():
                if i.id == n:
                    e = i
                    w = i
                if i.id == r:
                    t = i
                    a = i.address
                    b = i.coords
                    c = i.notes
            t.address = w.address
            t.coords = w.coords
            t.notes = w.notes
            e.address = a
            e.coords = b
            e.notes = c
            db_sess.commit()

    def ref(self):
        ml = ML()
        self.dialogs.append(ml)
        ml.show()

    def sh(self):
        v = View()
        self.dialogs.append(v)
        v.show()

    def li(self):
        li = List()
        self.dialogs.append(li)
        li.show()


class ML(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        db_session.global_init("db/project.db")
        db_sess = db_session.create_session()
        k = db_sess.query(Place).first()
        t = k.coords.split()
        api_server = "http://static-maps.yandex.ru/1.x/"
        lon = t[0]
        lat = t[1]
        spn = '0.005'
        params = {
            "ll": ",".join([lon, lat]),
            "spn": ",".join([spn, spn]),
            "l": "map"
        }
        response = requests.get(api_server, params=params)
        map_file = "map.jpg"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.dialogs = []
        self.setupUi(self)
        self.pushButton.clicked.connect(self.rg)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(len(db_sess.query(Place).all()) + 1)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("id"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Адресс"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Координаты"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Заметки"))
        x = 1
        for i in db_sess.query(Place).all():
            self.tableWidget.setItem(x, 0, QTableWidgetItem(str(i.id)))
            self.tableWidget.setItem(x, 1, QTableWidgetItem(str(i.address)))
            self.tableWidget.setItem(x, 2, QTableWidgetItem(i.coords))
            self.tableWidget.setItem(x, 3, QTableWidgetItem(i.notes))
            x += 1
        self.initUI("map.jpg")

    def initUI(self, a):
        self.pixmap = QPixmap(a)
        self.label_2.setPixmap(self.pixmap)

    def rg(self):
        db_session.global_init("db/project.db")
        db_sess = db_session.create_session()
        t = len(db_sess.query(Place).all())
        dlg = New()
        dlg.exec()
        s = dlg.ui
        x = s.lineEdit.text()
        y = int(s.lineEdit_2.text())
        if y > t + 1:
            y = t + 1
        z = s.textBrowser.toPlainText()
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?" \
                           f"apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={x}&format=json"
        response = requests.get(geocoder_request)
        if response:
            json_response = response.json()
            add= json_response["response"]["GeoObjectCollection"]["featureMember"][0][
                "GeoObject"]['metaDataProperty'][
                'GeocoderMetaData']['text']
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            coords = toponym["Point"]["pos"]
        c = list(db_sess.query(Place).all())
        c.reverse()
        for i in c:
            if i.id >= y:
                i.id = i.id + 1
                db_sess.commit()
        news = Place(id=y,
                     address=add,
                     coords=coords,
                     notes=z)
        db_sess.add(news)
        db_sess.commit()


class List(QMainWindow, Ui_List):
    def __init__(self):
        global app1
        super().__init__()
        self.dialogs = []
        self.setupUi(self)
        self.label_2 = QWebEngineView()
        self.label_2.setGeometry(QtCore.QRect(44, 95, 871, 601))
        print(1)
        self.label_2.load(QUrl('https://www.python.org/downloads/'))

class View(QMainWindow, Viv):
    def __init__(self):
        super().__init__()
        self.dialogs = []
        self.setupUi(self)
        db_session.global_init("db/project.db")
        db_sess = db_session.create_session()
        k = db_sess.query(Place).first()
        t = k.coords.split()
        p = k.address
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?" \
                           f"apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={p}&format=json"
        response = requests.get(geocoder_request)
        if response:
            json_response = response.json()
            add = json_response["response"]["GeoObjectCollection"]["featureMember"][0][
                "GeoObject"]['metaDataProperty'][
                'GeocoderMetaData']['text']
        self.label.setText(add)
        api_server = "http://static-maps.yandex.ru/1.x/"
        lon = t[0]
        lat = t[1]
        spn = '0.005'
        params = {"ll": ",".join([lon, lat]),
                  "spn": ",".join([spn, spn]),
                  "l": "map"
                  }
        response = requests.get(api_server, params=params)
        map_file = "view.jpg"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.initUI("view.jpg")
        self.max = len(db_sess.query(Place).all())
        self.x = 1
        self.pushButton.clicked.connect(self.tre)
        self.pushButton_2.clicked.connect(self.kli)

    def set(self):
        db_session.global_init("db/project.db")
        db_sess = db_session.create_session()
        k = ''
        for i in db_sess.query(Place).filter(Place.id == self.x):
            k = i
        if k:
            t = k.coords.split()
            api_server = "http://static-maps.yandex.ru/1.x/"
            lon = t[0]
            lat = t[1]
            spn = '0.005'
            params = {
                "ll": ",".join([lon, lat]),
                "spn": ",".join([spn, spn]),
                "l": "map"
            }
            response = requests.get(api_server, params=params)
            map_file = "view.jpg"
            with open(map_file, "wb") as file:
                file.write(response.content)
            self.initUI("view.jpg")
            p = k.address
            geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?" \
                               f"apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={p}&format=json"
            response = requests.get(geocoder_request)
            if response:
                json_response = response.json()
                add = json_response["response"]["GeoObjectCollection"]["featureMember"][0][
                    "GeoObject"]['metaDataProperty'][
                    'GeocoderMetaData']['text']
            self.label.setText(add)

    def kli(self):
        self.x += 1
        if self.x >= self.max:
            self.x = 1
        self.set()

    def tre(self):
        self.x -= 1
        if self.x < 1:
            self.x = self.max - 1
        self.set()

    def initUI(self, a):
        self.pixmap = QPixmap(a)
        self.label_2.setPixmap(self.pixmap)


class New(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class R(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ren()
        self.ui.setupUi(self)


class D(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Dl()
        self.ui.setupUi(self)


@app1.route('/')
def bootstrap():
    return render_template('index.html')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())