import sys
from PyQt5.QtGui import QKeySequence, QPixmap
from PyQt5.QtWidgets import QMainWindow, QShortcut, QApplication
from PyQt5 import uic
import requests


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(600, 550)
        uic.loadUi('main_window.ui', self)

        self.map_ll = ['37', '55']
        self.map_zoom = 1
        self.map_l = 'map'
        self.url_map = 'http://static-maps.yandex.ru/1.x/'

        self.pgup = QShortcut(QKeySequence("PgUp"), self).activated.connect(self.uppp)
        self.pgdn = QShortcut(QKeySequence("PgDown"), self).activated.connect(self.downnn)
        self.down = QShortcut(QKeySequence("Down"), self).activated.connect(self.down)
        self.left = QShortcut(QKeySequence("Left"), self).activated.connect(self.leftr)
        self.pgup = QShortcut(QKeySequence("Right"), self).activated.connect(self.right)
        self.pgup = QShortcut(QKeySequence("Up"), self).activated.connect(self.up)

        self.refresh_map()
        self.show()


    def up(self):
        self.map_ll[1] = str(int(self.map_ll[1]) + 1)
        self.refresh_map()

    def right(self):
        self.map_ll[0] = str(int(self.map_ll[0]) + 1)
        self.refresh_map()

    def leftr(self):
        self.map_ll[0] = str(int(self.map_ll[0]) - 1)
        self.refresh_map()

    def down(self):
        self.map_ll[1] = str(int(self.map_ll[1]) - 1)
        self.refresh_map()

    def uppp(self):
        self.map_zoom += 0.15
        self.refresh_map()

    def downnn(self):
        self.map_zoom -= 0.15
        self.refresh_map()

    def set_coor(self, coor):
        self.map_ll = list(coor)

    def refresh_map(self):
        map_params = {
            'l': self.map_l,
            'll': ','.join(self.map_ll),
            'spn': f"{self.map_zoom},{self.map_zoom}"
        }
        response = requests.get(self.url_map, map_params)
        with open('tmp.jpg', mode='wb') as tmp:
            tmp.write(response.content)
        pixmap = QPixmap()
        pixmap.load('tmp.jpg')
        self.g_map.setPixmap(pixmap)


app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
