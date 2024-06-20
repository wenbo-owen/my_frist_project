# 校验器是用来限制文本框输入的


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp


class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator,self).__init__()
        self.initUI()
        print('123')

    def initUI(self):
        self.setWindowTitle('校验器')

        #创建表单布局
        formlayout = QFormLayout()

        #创建3个QLineEdit控件
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        # 将3个控件添加到表单中
        formlayout.addRow('整数类型',intLineEdit)
        formlayout.addRow('浮点类型',doubleLineEdit)
        formlayout.addRow('数字和字母',validatorLineEdit)

        #设置提示文本
        intLineEdit.setPlaceholderText('整型')
        doubleLineEdit.setPlaceholderText('浮点型')
        validatorLineEdit.setPlaceholderText('字母和数字')

        #整数校验器[1,99]
        intValidator = QIntValidator(self)
        intValidator.setRange(1,99)


        #浮点校验器 [-360,360],小数点后两位
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360.00,360.00)
        doubleValidator.setNotation(doubleValidator.StandardNotation)
        #精度小数点后2位
        doubleValidator.setDecimals(2)

        #字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # LineEdit 设置校验器 校验器和控件绑定
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        # 设置布局
        self.setLayout(formlayout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QLineEditValidator()
    w.show()
    sys.exit(app.exec_())