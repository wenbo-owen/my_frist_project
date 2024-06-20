import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QMainWindow,QWidget,QHBoxLayout
from PyQt5.QtGui import QIcon

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')

        self.button1 = QPushButton('退出应用程序')
        self.button1.clicked.connect(self.onClik_Button)

        layout = QHBoxLayout()
        #将button1 装载到layout中
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    #按钮单击时间的方法(自定义的槽)
    def onClik_Button(self):
        sender = self.sender()
        print(sender.text()+'被按下')
        app = QApplication.instance()
        #退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/cartoon5.ico'))
    win = QuitApplication()
    win.show()
    # 进入程序的主循环
    sys.exit(app.exec_())