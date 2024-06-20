import sys
from PyQt5.QtWidgets import QApplication, QMainWindow ,QToolTip,QPushButton,QWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QFont

class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm,self).__init__()
        self.initUI()
        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('这是一个按钮')
        layout= QHBoxLayout()
        layout.addWidget(self.button1)
        print('hello mg')

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300, 300,300,300)
        self.setWindowTitle('设置控件提示信息')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TooltipForm()
    win.show()
    sys.exit(app.exec_())
