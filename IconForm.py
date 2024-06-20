import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon
#继承于父类，那一定比父类更加丰富

class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300,250,250)
        # 设置主窗口的标题
        self.setWindowTitle('设置窗口图标')
        #设置窗口图形
        self.setWindowIcon(QIcon('./image/cartoon5.ico'))






    # def center(self):
    #     screen = QDesktopWidget().screenGeometry()
    #     size = self.geometry()
    #
    #     newLeft = (screen.width() - size.width())/2
    #     newTop = (screen.height() - size.height())/2
    #
    #     self.move(newLeft, newTop)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./image/cartoon5.ico'))
    win = IconForm()
    win.show()
    #进入程序的主循环
    sys.exit(app.exec_())