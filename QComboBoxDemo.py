'''
下拉列表控件(QComboBox)
1. 如何将列表项添加到QComBox控件中
2. 如何获取选中的列表项
'''

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件')
        self.resize(300,100)
        layout = QVBoxLayout()
        self.label = QLabel('请选择编程语言')
        self.cb = QComboBox()
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        self.cb.addItems(['Java','C#','Ruby'])
        self.cb.currentIndexChanged.connect(self.selectionChanged)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)


    def selectionChanged(self,i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()

        for count in range(self.cb.count()):
            # print('item' + str(count) +'=' + self.cb.itemText(count))
            print('current index' , i , 'selection changed' , str(count) +'=' + self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QComboBoxDemo()
    demo.show()
    sys.exit(app.exec_())