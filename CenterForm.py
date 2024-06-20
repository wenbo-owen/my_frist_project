import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon
#继承于父类，那一定比父类更加丰富

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()
    # 设置主窗口的标题
        self.setWindowTitle('让窗口居中')
        self.resize(400,300)
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()

        newLeft = (screen.width() - size.width())/2
        newTop = (screen.height() - size.height())/2

        self.move(newLeft, newTop)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/cartoon5.ico'))
    win = CenterForm()
    win.show()
    #进入程序的主循环
    sys.exit(app.exec_())