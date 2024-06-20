import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QWidget,QApplication,QPushButton


class ScreenGeometry(QWidget):
    def __init__(self):
        super(ScreenGeometry,self).__init__()

        self.btn = QPushButton(self)
        self.btn.setText('按钮')
        self.btn.move(24,52)
        self.btn.clicked.connect(self.onClick_Button)
        self.resize(300,240)
        self.move(250,200)
        self.setWindowTitle('屏幕坐标系')


    def onClick_Button(self):
        print("onclick")
        # print(f"widget.x() = {self.x()}")
        print("1")
        print("widget.x()=%d" % self.x())
        print("widget.y()=%d" % self.y())
        print("widget.width()=%d" % self.width())
        print("widget.height()=%d" % self.height())

        print("2")
        print("widget.geometry().x()=%d" % self.geometry().x())
        print("widget.geometry().y()=%d" % self.geometry().y())
        print("widget.geometry().width()=%d" % self.geometry().width())
        print("widget.geometry().height()=%d" % self.geometry().height())

        print("3")
        print("widget.frameGeometry().x()=%d" % self.frameGeometry().x())
        print("widget.frameGeometry().y()=%d" % self.frameGeometry().y())
        print("widget.frameGeometry().width()=%d" % self.frameGeometry().width())
        print("widget.frameGeometry().height()=%d" % self.frameGeometry().height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ScreenGeometry()
    win.show()
    sys.exit(app.exec_())