import sys

from PyQt5.QtCore import Qt, pyqtSignal, QTime, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout


class TimerLabel(QWidget):
    stopped = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__startHour = 0
        self.__startMin = 0
        self.__startSec = 0

        self.__startTime = QTime()
        self.__endTime = QTime()

        self.__timer = QTimer(self)
        self.__timer_interval = -1

        self.__lbl = QLabel()

    def __initUi(self):
        self.setStartHMS()
        self.__lbl.setAlignment(Qt.AlignCenter)
        self.__lbl.setFont(QFont('Arial', 24))
        lay = QGridLayout()
        lay.addWidget(self.__lbl)
        self.setLayout(lay)

    def setTimerReverse(self, f: bool):
        if f:
            self.__timer_interval = -1
        else:
            self.__timer_interval = 1

    def setStartHMS(self):
        self.__startTime.setHMS(self.__startHour, self.__startMin, self.__startSec)
        time_left_text = self.__startTime.toString('hh:mm:ss')
        self.__lbl.setText(time_left_text)

    def setEndHMS(self):
        self.__startTime.setHMS(self.__startHour, self.__startMin, self.__startSec)
        time_left_text = self.__startTime.toString('hh:mm:ss')
        self.__lbl.setText(time_left_text)

    def setStartHour(self, h):
        self.__startHour = h
        self.setStartHMS()

    def setStartMinute(self, m):
        self.__startMin = m
        self.setStartHMS()

    def setStartSecond(self, s):
        self.__startSec = s
        self.setStartHMS()

    def setEndHour(self, h):
        pass

    def setEndMinute(self, m):
        pass

    def setEndSecond(self, s):
        pass

    def __prepareToTimer(self):
        self.__timerTicking()

    def start(self):
        self.__timer.timeout.connect(self.__timerTicking)
        self.__timer.singleShot(self.__startTime.msec(), self.__prepareToTimer)
        # update the timer every second
        self.__timer.start(1000)

    def __timerTicking(self):
        try:
            self.__startTime = self.__startTime.addSecs(self.__timer_interval)
            time_left_text = self.__startTime.toString('hh:mm:ss')
            self.__lbl.setText(time_left_text)
            if self.__endTime == time_left_text:
                self.__stop()
            else:
                pass
        except Exception as e:
            print(e)
            print(sys.exc_info()[2].tb_lineno)
            print(sys.exc_info())

    def __stop(self):
        try:
            self.__startTime = QTime(self.__startHour, self.__startMin, self.__startSec)
            self.__lbl.setText(self.__startTime.toString("hh:mm:ss"))

            self.__timer.stop()

            self.__timer.timeout.disconnect(self.__timerTicking)

        except Exception as e:
            print(e)
            print(sys.exc_info()[2].tb_lineno)
            print(sys.exc_info())

