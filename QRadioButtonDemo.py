'''
单选按钮控件 ：Radio Button Demo
'''


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class RadioButtonDemo(QWidget):
    def __init__(self):
        super(RadioButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Radio Button Demo')
        layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)


        self.button2 = QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def buttonState(self):
        #于获取发出信号的对象git
        radioButton = self.sender()

        if radioButton.isChecked() == True:
            print( '<' + radioButton.text() +'>被选中')
        else:
            print('<' + radioButton.text() + '>被取消选中状态')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = RadioButtonDemo()
    demo.show()
    sys.exit(app.exec_())