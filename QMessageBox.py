'''
消息对话框：QMessageBox
1. 关于对话框
2. 错误对话框
3. 警告对话框
4.提醒对话框
5.警告对话框

有2点差异
1. 显示的对话框图标可能不一样
2. 显示的按钮是不一样的
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBox鼠子')
        self.resize(300,400)
        layout = QVBoxLayout()
        self.button1 = QPushButton()
        self.button1.setText('显示关于对话框')
        self.button1.clicked.connect(self.showDialog)

        self.button2 = QPushButton()
        self.button2.setText('显示消息对话框')
        self.button2.clicked.connect(self.showDialog)

        self.button3 = QPushButton()
        self.button3.setText('显示警告对话框')
        self.button3.clicked.connect(self.showDialog)

        self.button4 = QPushButton()
        self.button4.setText('显示错误对话框')
        self.button4.clicked.connect(self.showDialog)

        self.button5 = QPushButton()
        self.button5.setText('显示提问对话框')
        self.button5.clicked.connect(self.showDialog)

        # 布局显示，如果类继承QMainWindow，
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        self.setLayout(layout)

    #QMessage相当于一个模块
    def showDialog(self):
        text = self.sender().text()
        if text == '显示关于对话框':
            QMessageBox.about(self,'关于','这是一个关于对话框')
        elif text == '显示消息对话框':
            #QMessageBox.Yes | QMessageBox.No 这里多增加了2个按键
            reply = QMessageBox.information(self,'消息','这是一个消息对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            print(reply == QMessageBox.Yes)
        elif text == '显示警告对话框':
            QMessageBox.warning(self,'警告','这个一个警告对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        elif text == '显示错误对话框':
            QMessageBox.critical(self,'错误','这是一个错误对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        elif text == '显示提问对话框':
            QMessageBox.question(self,'提问','这是一个提问对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QMessageBoxDemo()
    demo.show()
    sys.exit(app.exec_())