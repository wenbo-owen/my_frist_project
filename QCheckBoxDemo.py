'''
    复选框控件(QCheckBox)
    3种状态
    未选中：0
    半选中：1
    选中：2
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo,self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('复选框控件演示')
        layout = QHBoxLayout()
        self.checkBox1 = QCheckBox('复选框控件1')
        self.checkBox1.setChecked(True)
        
        self.checkBox2 = QCheckBox('复选框控件2')
        self.checkBox2.setChecked(True)

        self.checkBox3 = QCheckBox('半选中')
        self.checkBox3.setTristate(True)
        self.checkBox3.setChecked(Qt.PartiallyChecked)

        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        layout.addWidget(self.checkBox3)
        self.checkBox1.stateChanged.connect(lambda:self.checkState(self.checkBox1))
        self.checkBox2.stateChanged.connect(lambda:self.checkState(self.checkBox2))
        self.checkBox3.stateChanged.connect(lambda: self.checkState(self.checkBox3))

        # self.checkBox1.stateChanged.connect(self.checkState)
        # self.checkBox2.stateChanged.connect(self.checkState)
        # self.checkBox3.stateChanged.connect(self.checkState)



        self.setLayout(layout)

    def checkState(self,cb):
        check1Status = cb.text() + ',isChecked=' + str(cb.isChecked()) +',checkState=' + str(cb.checkState()) + '\n'
        # check2Status = self.checkBox2.text() + ',isChecked=' + str(self.checkBox2.isChecked()) + ',checkState=' + str(self.checkBox2.checkState()) + '\n'
        # check2Status = self.checkBox3.text() + ',isChecked=' + str(self.checkBox3.isChecked()) + ',checkState=' + str(self.checkBox3.checkState()) + '\n'
        print(check1Status)

    # def checkState(self, cb):
    #     check1Status = cb.text() + ',isChecked=' + str(cb.isChecked()) + ',checkState=' + str(cb.checkState()) + '\n'
    #     # check2Status = self.checkBox2.text() + ',isChecked=' + str(self.checkBox2.isChecked()) + ',checkState=' + str(self.checkBox2.checkState()) + '\n'
    #     # check2Status = self.checkBox3.text() + ',isChecked=' + str(self.checkBox3.isChecked()) + ',checkState=' + str(self.checkBox3.checkState()) + '\n'
    #     print(check1Status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QCheckBoxDemo()
    demo.show()
    sys.exit(app.exec_())