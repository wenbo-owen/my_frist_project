
import sys
from PyQt5.QtWidgets import *

class QLabelEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        print('134')

    def initUI(self):

        formlayout = QFormLayout()
        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoLineEdit = QLineEdit()

        formlayout.addRow("Normal", normalLineEdit)
        formlayout.addRow("Echo", noEchoLineEdit)
        formlayout.addRow("Password", passwordLineEdit)
        formlayout.addRow("PasswordEcho", passwordEchoLineEdit)

        #placeholdertext
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoLineEdit.setPlaceholderText("PasswordEcho")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        # 应用表单布局
        self.setLayout(formlayout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelEchoMode()
    main.show()
    sys.exit(app.exec_())

