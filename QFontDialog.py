'''

字体对话框：QFontDialog

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QFontDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('FontDialog例子')
        layout = QVBoxLayout()
        self.fontButton = QPushButton('选择字体')
        self.fontButton.clicked.connect(self.getFont)

        self.fontLabel = QLabel('Hello,米果')
        layout.addWidget(self.fontButton)
        layout.addWidget(self.fontLabel)
        self.setLayout(layout)

    def getFont(self):
        font,ok = QFontDialog.getFont()  #获取字体
        if ok: #字体获取成功
            self.fontLabel.setFont(font)
            print(str(font))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())