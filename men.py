import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(5,30,1355,730)
        self.browser=QWebEngineView()
        # Загрузить внешний веб-интерфейс
        self.browser.load(QUrl('https://blog.csdn.net/jia666666'))
        self.setCentralWidget(self.browser)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec_())