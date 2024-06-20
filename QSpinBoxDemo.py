'''

    QSpinBox (计数器控件)
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSpinBoxDemo')
        self.resize(200,100)

        layout = QVBoxLayout()
        self.label = QLabel('当前值')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.spinBox = QSpinBox()
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setValue(18)
        self.spinBox.setRange(0,255)
        self.spinBox.setSingleStep(3)


        layout.addWidget(self.spinBox)
        self.spinBox.valueChanged.connect(self.valueChanged)
        self.setLayout(layout)
    def valueChanged(self):
        self.label.setText('当前值'+str(self.spinBox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QSliderDemo()
    demo.show()
    sys.exit(app.exec_())