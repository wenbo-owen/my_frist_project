import threading
import sys
import time                             # 定时器
import serial
from datetime import datetime
import serial.tools.list_ports
from uart_ui import Ui_MainWindow

from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtCore import (QTimer, pyqtSignal)
from PyQt5.QtWidgets import (QMainWindow, QApplication)
import base64, os



class SerialTool(QMainWindow, Ui_MainWindow):
    signalRecieve = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.refreshPort()
        self.InitUIEvent()              #初始化ui事件   ******
        self.initCOM()                  #串口初始化

        self.signalRecieve.connect(self.uart_receive_display)

        # 创建定时发送定时器 这个定时器很有趣
        self.timer_send = QTimer(self)
        self.timer_send.timeout.connect(self.UartSend)




    #刷新串口，读取串口设备
    def refreshPort(self):
        self.com_list = []
        port_list = list(serial.tools.list_ports.comports())
        self.Combo_COM.clear()
        if len(port_list) > 0:
            for port_com in port_list:
                port_serial = list(port_com)[0]
                self.Combo_COM.addItem(port_serial)
                self.com_list.append(port_serial)
        else:
            self.Combo_COM.addItem('')

    # 初始化串口，我认为这里是装载UI界面上默认的参数
    def initCOM(self):
        self.l_serial = serial.Serial()             # l_serial就是一个串口对象
        if (len(self.com_list)):
            self.l_serial.port = self.com_list[0]
        self.l_serial.baudrate = int(self.Combo_Baudrate.currentText())
        self.l_serial.bytesize = int(self.Combo_Data_bit.currentText())
        self.l_serial.stopbits = int(self.Combo_Stop_bit.currentText())
        self.l_serial.parity = self.Combo_Parity.currentText()
        # serial.PARITY_NONE
        self.l_serial.timeout = 0.2

    def InitUIEvent(self):
            self.Combo_COM.activated[str].connect(self.ComActivated)                # 串口port属性
            self.Combo_COM.popupAboutToBeShown.connect(self.RefreshComActivated)
            self.Combo_Baudrate.activated[str].connect(self.BaudActivated)
            self.Combo_Parity.activated[str].connect(self.ParityBitActivated)
            self.Combo_Data_bit.activated[str].connect(self.DataBitActivated)
            self.Combo_Stop_bit.activated[str].connect(self.StopBitActivated)

            self.Button_Onoff_com.clicked[bool].connect(self.StartComActivated)
            self.Button_Clear_display.clicked.connect(self.ClearReceiveActivated)
            self.Box_Display_hex.stateChanged.connect(lambda: self.CheckActivated(self.Box_Display_hex))
            self.Box_Auto_wrap.stateChanged.connect(lambda: self.CheckActivated(self.Box_Auto_wrap))
            self.Box_Display_send.stateChanged.connect(lambda: self.CheckActivated(self.Box_Display_send))
            self.Box_Display_time.stateChanged.connect(lambda: self.CheckActivated(self.Box_Display_time))
            #
            #
            self.Box_Periodic_send.stateChanged.connect(lambda: self.CheckActivated(self.Box_Periodic_send))
            self.Box_Hex_send.stateChanged.connect(lambda: self.CheckActivated(self.Box_Hex_send))
            #
            self.Button_Clear_send.clicked.connect(self.ClearSendActivated)
            self.Button_Send.clicked.connect(self.UartSend)

    # 串口对象的port属性
    def ComActivated(self, text):
        self.l_serial.port = text
        print(text)


    def RefreshComActivated(self):
        self.refreshPort()
        if (len(self.com_list)):
            self.l_serial.port = self.com_list[0]
            # print(l_serial.port)
        print(self.com_list[0])

    def BaudActivated(self, text):
        self.l_serial.baudrate = int(text)
        print(text)

    def ParityBitActivated(self, text):
        print(text)
        if (text == 'N'):
            self.l_serial.parity = serial.PARITY_NONE
        elif (text == 'O'):
            self.l_serial.parity = serial.PARITY_ODD
        elif (text == 'E'):
            self.l_serial.parity = serial.PARITY_EVEN

    def DataBitActivated(self, text):
        self.l_serial.bytesize = int(text)

    def StopBitActivated(self, text):
        self.l_serial.stopbits = int(text)

    def ClearReceiveActivated(self):
        self.Textbrowser_Receive.setPlainText('')


    #启动，停用串口功能
    def StartComActivated(self):

        if self.l_serial.isOpen():
            self.timer_send.stop()
            # self.thread_read.join()
            self.l_serial.close()
            self.Button_Onoff_com.setText("打开串口")

            self.Combo_COM.setEnabled(True)
            self.Combo_Baudrate.setEnabled(True)
            self.Combo_Data_bit.setEnabled(True)
            self.Combo_Stop_bit.setEnabled(True)
            self.Combo_Parity.setEnabled(True)
        else:
            self.l_serial.open()
            self.Button_Onoff_com.setText("关闭串口")

            self.Combo_COM.setEnabled(False)
            self.Combo_Baudrate.setEnabled(False)
            self.Combo_Data_bit.setEnabled(False)
            self.Combo_Stop_bit.setEnabled(False)
            self.Combo_Parity.setEnabled(False)

            self.thread_read = None
            self.thread_read = threading.Thread(target=self.UartRead)
            self.thread_read.setDaemon(True)
            self.thread_read.start()

    def uart_receive_display(self, obj):
        now_time = datetime.now()  # 获取当前时间
        new_time = now_time.strftime('[%H:%M:%S:%f]')
        if self.Box_Display_hex.checkState():  # hex显示
            if (self.Box_Display_time.checkState()):  # 显示时间
                self.recv_data = '\r\n' + new_time + obj.strip()
            else:
                self.recv_data = obj.strip()
            if self.Box_Display_send.checkState():  # 显示发送
                self.recv_data = '\r\n' + '[Receive]:' + self.recv_data

            if self.Box_Auto_wrap.checkState():
                self.Textbrowser_Receive.append(self.recv_data)
            else:
                self.Textbrowser_Receive.insertPlainText(self.recv_data)
            # self.Textbrowser_Receive.append(self.recv_data)
        else:
            if self.Box_Display_time.checkState():
                self.recv_data = '\r\n' + new_time + obj.decode('utf-8', "ignore")
            else:
                self.recv_data = obj.decode('utf-8', "ignore")

            if self.Box_Display_send.checkState():
                self.recv_data = '\r\n' + '[Receive]:' + self.recv_data

            if self.Box_Auto_wrap.checkState():
                self.Textbrowser_Receive.append(self.recv_data)
            else:
                self.Textbrowser_Receive.insertPlainText(self.recv_data)

        self.Textbrowser_Receive.moveCursor(self.Textbrowser_Receive.textCursor().End)  # 文本框显示到底部

    # time.sleep(0.2)
    # 串口读函数
    def UartRead(self):
        while self.l_serial.isOpen():
            num = self.l_serial.inWaiting()
            if num:
                self.data = self.l_serial.read(num)
                if self.Box_Display_hex.checkState():  # 16进制接收  就是哪个 hex check_box
                    hex_data = ''
                    for i in range(0, len(self.data)):
                        hex_data = hex_data + '{:02X}'.format(self.data[i]) + ' '
                    # self.Textbrowser_Receive.append(hex_data.strip())
                    self.signalRecieve.emit(hex_data)
                else:
                    # self.Textbrowser_Receive.append(data.decode().strip())
                    # self.Textbrowser_Receive.insertPlainText(data.decode('utf-8',"ignore"))
                    self.signalRecieve.emit(self.data)

            time.sleep(0.1)

    def CheckActivated(self, BtnCheck):
        if BtnCheck == self.Box_Periodic_send:
            if self.Box_Periodic_send.checkState():
                time = self.LineEdit_Ms.text()
                time_val = int(time, 10)
                if time_val > 0:
                    self.timer_send.start(time_val)
            else:
                self.timer_send.stop()

    #发射区， 《清除》 按键
    def ClearSendActivated(self):
        self.TextEdit_Send.setPlainText('')

    #发射区， 《发送》按键
    def UartSend(self):
        InputStr = self.TextEdit_Send.toPlainText()   # 读textedit中的字符串
        if InputStr == "":
            return

        if self.Box_Display_send.checkState():              # 接收区 《显示发送》 chenk_box
            self.recv_data = '[Send]:' + InputStr           # 增加前头的[send]: 标头
            self.Textbrowser_Receive.append(self.recv_data) #Textbrowser_Receive 增加字符串，此时Textbrowser_Receive中
                                                            #会显示这行发送字符串
        # 验证功能先屏蔽这段if
        if self.Box_Hex_send.checkState():                  # hex Check_box

            InputStr = InputStr.strip()                     #删除前后的空格
            send_list = []
            while InputStr != '':

                try:
                    num = int(InputStr[0:2], 16)

                except ValueError:
                    QMessageBox.critical(self, 'pycom', '请输入十六进制数据，以空格分开!')
                    return None

                InputStr = InputStr[2:]
                InputStr = InputStr.strip()

                # 添加到发送列表中
                send_list.append(num)


            print(send_list)
            InputStr = bytes(send_list)         # while循环退出后，将send_list 转换成字节 赋值给InputStr，转换为字节型


            self.l_serial.write(InputStr)
        else:
            self.l_serial.write(InputStr.encode())
            print(InputStr.encode())
            str1 = InputStr.replace(" ","")
            for char in str1:
                print(ord(char))



if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = SerialTool()

    ex.show()

    sys.exit(app.exec_())