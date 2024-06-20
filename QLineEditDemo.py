'''
QLineEdit 综合案例

'''


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('黄河这是一个QLineEdit综合小程序')

        edit1 = QLineEdit()
        # 使用init校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial',20))



        edit2 = QLineEdit()
        # 使用浮点型校验器
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        edit3 = QLineEdit()
        edit3.setInputMask('99_999_99999;#')

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChanged)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPressed)


        edit6 = QLineEdit('Hello MG')
        edit6.setReadOnly(True)



        formLayout = QFormLayout()

        formLayout.addRow('整数校验',edit1)
        formLayout.addRow('浮点数校验',edit2)
        formLayout.addRow('Input Mask', edit3)
        formLayout.addRow('文本变化',edit4)
        formLayout.addRow('密码', edit5)
        formLayout.addRow('只读', edit6)
        self.setLayout(formLayout)


    def textChanged(self, text):
        print('输入的内容'+text)

    def enterPressed(self):
        print('已输入值')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()
    sys.exit(app.exec_())

