'''

滑块控件（QSlider）
滑块控件

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
        self.setWindowTitle('QSliderDemo')
        self.resize(300,700)
        layout = QVBoxLayout()
        self.label = QLabel('你好 米果 Pyqt5')
        self.label.setAlignment(Qt.AlignCenter) #中心对齐
        layout.addWidget(self.label)

        #------------------------------------------------------
        self.slider = QSlider(Qt.Horizontal)    # 水平滑块
        self.slider.setMinimum(12)  #设置最小值
        self.slider.setMaximum(48)  #设置最大值
        self.slider.setSingleStep(3) #设置步长
        self.slider.setValue(18)    #设置当前值
        # 设置刻度的位置 下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        #设置刻度的间隔
        self.slider.setTickInterval(6)
        layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.valueChanged)

        #----------------------------------------------------------
        self.slider1 = QSlider(Qt.Vertical)  # 垂直滑块
        self.slider1.setMinimum(10)  # 设置最小值
        self.slider1.setMaximum(60)  # 设置最大值
        self.slider1.setSingleStep(5)  # 设置步长
        self.slider1.setValue(30)  # 设置当前值
        # 设置刻度的位置
        self.slider1.setTickPosition(QSlider.TicksRight)
        # 设置刻度的间隔
        self.slider1.setTickInterval(2)
        layout.addWidget(self.slider1)
        self.slider1.valueChanged.connect(self.valueChanged)




        self.setLayout(layout)

    def valueChanged(self):
        print('当前值 %s' % self.sender().value())
        size = self.sender().value()
        self.label.setFont(QFont('Arial',size))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QSliderDemo()
    demo.show()
    sys.exit(app.exec_())
