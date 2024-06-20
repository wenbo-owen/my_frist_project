import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class DrawPointsDemo(QWidget):
    def __init__(self):
        super(DrawPointsDemo,self).__init__()
        self.setWindowTitle('在窗口上用像素点绘制2个周期的正弦曲线')
        self.resize(300,300)

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.blue)

        size = self.size()
        for i in range(1000):

            x = 100 *(-1 + 2.0 * i/1000) + size.width()/2.0
            y = -50*math.sin((x-size.width()/2.0)* math.pi/50)+size.height()/2.0

            print(f'x={x},y={y}')

            painter.drawPoint(int(x),int(y))

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawPointsDemo()
    ex.show()
    sys.exit(app.exec_())


