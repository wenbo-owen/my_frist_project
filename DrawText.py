import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter,QFont,QColor
from PyQt5.QtCore import Qt


class DrawTextDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(500,200)
        self.text = 'Python从菜鸟到高手'
    def paintEvent(self,event):
        painter = QPainter(self)
        painter.begin(self)
        print('aa')
        painter.setPen(QColor(150,43,5))

        painter.setFont(QFont('SimSun',25))
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DrawTextDemo()
    demo.show()
    sys.exit(app.exec_())