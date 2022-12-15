# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Clock(QMainWindow):
    def __init__(self):
        super().__init__()
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

        self.setWindowTitle('Clock')
        self.setGeometry(200, 200, 300, 300)

        self.hPointer = QtGui.QPolygon([QPoint(6, 7),
                                        QPoint(-6, 7),
                                        QPoint(0, -50)])
        
        self.mPointer = QtGui.QPolygon([QPoint(6, 7),
                                        QPoint(-6, 7),
                                        QPoint(0, -70)])
        
        self.sPointer = QtGui.QPolygon([QPoint(1, 1),
                                        QPoint(-1, 1),
                                        QPoint(0, -90)])
        
        self.bColor = Qt.green
        self.sColor = Qt.red

    def paintEvent(self, event):
        # getting the minimum width n height
        # so that the clock wopuld remain a square
        rec = min(self.width(), self.height())

        # getting current time
        tik = QTime.currentTime()

        # creating a painter object
        painter = QPainter(self)
        # argument : color rotation and which hand should b pointed

        def drawPointer(color, rotation, pointer):

        # setting the brush
            painter.setBrush(QBrush(color))

        # saving painter
            painter.save()

        # rotating painter
            painter.rotate(rotation)

        # drawing the polygon
            painter.drawConvexPolygon(pointer)

        # restore the painter
            painter.restore()
    
        # tune up painter
        painter.setRenderHint(QPainter.Antialiasing)

        # translating the painter
        painter.translate(self.width() / 2, self.height() / 2)

        # scale the painter
        painter.scale(rec / 200, rec / 200)

        # set current pen as no pen
        painter.setPen(QtCore.Qt.NoPen)
    
        # draw each hand
        drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
        drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
        drawPointer(self.sColor, (6 * tik.second()), self.sPointer)

        # drawing the background
        painter.setPen(QPen(self.bColor))

        for i in range(0, 60):
          # drawing background lines
            if (i % 5) == 0:
                painter.drawLine(87, 0, 97, 0)
                 # rotating the painter
            painter.rotate(6)
                # ending the painter
        painter.end()
        # Driver code
if __name__ == '__main__':

    app = QApplication(sys.argv)

    # creating a clock object
    win = Clock()

    # show
win.show()

exit(app.exec_())

