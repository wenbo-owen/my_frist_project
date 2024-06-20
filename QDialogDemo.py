import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QdialogDemo(QMainWindow):
    def __init__(self):
        super(QdialogDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)

        self.button = QPushButton(self)  #按键就在QMainWindow
        self.button.setText('弹出对话框')
        self.button.move(50,50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()  #创建一个Dialog
        dialog.setWindowTitle('鼠子对话框')
        button1 = QPushButton('确定',dialog)
        button1.move(50,50)
        button1.clicked.connect(dialog.close)
        #对话框以模式的状态显示
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QdialogDemo()
    ex.show()
    sys.exit(app.exec_())