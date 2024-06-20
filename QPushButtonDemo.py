import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *




class QPushButtonDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButtonDemo')
        self.resize(400, 300)
        layout = QVBoxLayout()
        self.button1 = QPushButton('第一个按钮')
        #self.button1.setText('Frist Button1')
        self.button1.setCheckable(True) #按钮按下不会抬起
        self.button1.toggle()
        # 这个self是QPushButtonDemo类
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonStatus)
        layout.addWidget(self.button1)

        #在文本前面显示图像

        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./image/pic2.jpg')))
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton('不可用按钮')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda:self.whichButton(self.button4))
        layout.addWidget(self.button4)


        self.setLayout(layout)


    def whichButton(self,btn):
        print('被单机的按钮是<' + btn.text() + '>')

    def buttonStatus(self):
        if self.button1.isChecked():  #是否被选中
            print('按键1已经被选中')
        else:
            print('按键1已经被释放')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
