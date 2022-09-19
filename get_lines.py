import os
import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 170, 661, 471))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 450, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 520, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 590, 141, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(810, 50, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 50, 491, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 50, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 170, 181, 251))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 110, 181, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Схема"))
        self.pushButton_2.setText(_translate("MainWindow", "Гибрид"))
        self.pushButton_3.setText(_translate("MainWindow", "Спутник"))
        self.pushButton_4.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_5.setText(_translate("MainWindow", "Сброс метки"))
        self.pushButton_6.setText(_translate("MainWindow", "Почтовый индекс"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self, a):
        super().__init__()
        self.setupUi(self)
        self.initUI(a)
        self.pushButton.clicked.connect(self.sh)
        self.pushButton_2.clicked.connect(self.gb)
        self.pushButton_3.clicked.connect(self.spu)
        self.pushButton_4.clicked.connect(self.get_addres)
        self.pushButton_5.clicked.connect(self.sbr)
        self.pushButton_6.clicked.connect(self.ind)

    def initUI(self, a):
        self.pixmap = QPixmap(a)
        self.image = self.label
        self.image.setPixmap(self.pixmap)

    def ind(self):
        global set, index, address
        if set:
            set = False
            self.textBrowser.setText(address)
        else:
            set = True
            self.textBrowser.setText(f'{address}\n{index}')

    def get_addres(self):
        global lon, lat, spn, pm, index, set, address
        add = self.lineEdit.text()
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": add,
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        json_response = response.json()
        k = json_response["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData']['text']
        a = json_response["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']["Point"]['pos']
        h = json_response["response"]['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData']['Address']['postal_code']
        a = a.split()
        address = k
        index = h
        if set:
            k = k + '\n' + h
        self.textBrowser.setText(k)
        lon = a[0]
        lat = a[1]
        spn = '0.005'
        pm = f"{a[0]},{a[1]},pmgrs"
        self.repic(lon, lat, spn, pm)

    def sbr(self):
        global lon, lat, spn, pm, address, index
        address = None
        index = None
        pm = None
        self.lineEdit.setText('')
        self.textBrowser.setText('')
        self.repic(lon, lat, spn, pm)

    def sh(self):
        global lon, lat, spn, pm
        spn = '0.002'
        self.repic(lon, lat, '0.002', pm)

    def gb(self):
        global lon, lat, spn, pm
        spn = '0.09'
        self.repic(lon, lat, '0.09', pm)

    def spu(self):
        global lon, lat, spn, pm
        spn = '50'
        self.repic(lon, lat, '50', pm)

    def keyPressEvent(self, event):
        global map_file, lon, lat, spn, pm
        spn = float(spn)
        lon, lat = float(lon), float(lat)
        if event.key() == Qt.Key_PageUp:
            spn *= 1.5
        elif event.key() == Qt.Key_PageDown:
            spn /= 1.5
        elif event.key() == Qt.Key_Down:
            lat -= 1.5 * spn
        elif event.key() == Qt.Key_Up:
            lat += 1.5 * spn
        elif event.key() == Qt.Key_Left:
            lon -= 1.5 * spn
        elif event.key() == Qt.Key_Right:
            lon += 1.5 * spn
        spn = str(spn)
        lon, lat = str(lon), str(lat)
        self.repic(lon, lat, spn, pm)

    def mousePressEvent(self, event):
        global spn, lon, lat
        a, b = float(lon), float(lat)
        spn = float(spn)
        if 220 <= event.x() <= 881 and 170 <= event.y() <= 641:
            x, y = event.x() - 220, event.y() - 170
            r = spn / 661 * x
            v = spn / 471 * y
            if x > 330:
                r = -r
            if y > 235:
                v = -v
            a += v
            b += r
        a, b = str(a), str(b)
        if (event.button() == Qt.LeftButton):
            self.find(a, b)
        print(a, b)

    def find(self, a, b):
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": f"{a},{b}",
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        json_response = response.json()
        print(json_response)

    def repic(self, lon, lat, spn, pm=None):
        global map_file
        os.remove(map_file)
        api_server = "http://static-maps.yandex.ru/1.x/"
        params = {
            "ll": ",".join([lon, lat]),
            "spn": ",".join([spn, spn]),
            "l": "map",
            "pt": pm
        }
        response = requests.get(api_server, params=params)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.initUI(map_file)


api_server = "http://static-maps.yandex.ru/1.x/"

lon = '37'
lat = '55'
spn = '0.002'
set = False
address = None
index = None
pm = None
params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([spn, spn]),
    "l": "map"
}
response = requests.get(api_server, params=params)
map_file = "map.png"
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example(map_file)
    ex.show()
    sys.exit(app.exec())
    os.remove(map_file)