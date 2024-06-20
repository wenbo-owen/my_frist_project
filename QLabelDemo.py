import sys
from PyQt5.QtWidgets import QApplication, QLabel,QMainWindow,QPushButton,QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import  QPalette,QPixmap
from PyQt5.QtCore import Qt

class QLableDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        print("HELLO")
    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color = yellow>这是一个文本标签</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()    #创建一个调色板对象
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        #不加链接的
        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('./image/pic2.jpg'))

        #如果设为True，用浏览器打开网页，如果设为False，调用槽函数
        label4.setOpenExternalLinks(True)
        label4.setText("<a href ='www.baidu.com'>感谢关注这个网站</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle ('Qlabel控件演示')

    def linkHovered(self):
        print("当鼠标滑过label2标签时，触发事件")

    def linkClicked(self):
        print("当鼠标点击label4标签时，触发事件")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLableDemo()
    main.show()
    sys.exit(app.exec_())
