import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
#继承于父类，那一定比父类更加丰富

class FristMainWin(QMainWindow):
    def __init__(self):
        super(FristMainWin, self).__init__()
    # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')
        self.resize(400,300)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒钟的消息',2000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/cartoon5.ico'))
    win = FristMainWin()
    win.show()
    #进入程序的主循环
    sys.exit(app.exec_())