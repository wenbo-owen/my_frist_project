
# mainlayout.addWidget(控件对象,rowIndex,columnIndex,row,column)

import sys
from PyQt5.QtWidgets import *

class QLabelBuddy(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()
        print('test123')

    def initUI(self):

        self.setWindowTitle('QLable与伙伴关系')

        nameLabel = QLabel('&Name',self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)                        #设置伙伴关系

        passwordLabel = QLabel('&Password',self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainlayout = QGridLayout(self)
        mainlayout.addWidget(nameLabel,0,0)
        mainlayout.addWidget(nameLineEdit, 0,1,1,2)
        mainlayout.addWidget(passwordLabel,1,0)
        mainlayout.addWidget(passwordLineEdit,1,1,1,2)
        mainlayout.addWidget(btnOK,2,1)
        mainlayout.addWidget(btnCancel,2,2)

        self.setLayout(mainlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QLabelBuddy()
    win.show()
    sys.exit(app.exec_())
