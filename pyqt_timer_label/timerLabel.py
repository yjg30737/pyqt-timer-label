import sys

from PyQt5.QtCore import Qt, pyqtSignal, QTime, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


class TimerLabel(QLabel):
    doubleClicked = pyqtSignal()
    stopped = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__start_hour = 0
        self.__start_min = 0
        self.__start_sec = 0

        self.__end_hour = 0
        self.__end_min = 0
        self.__end_sec = 0

        self.__startTime = QTime()
        self.__endTime = QTime()
        self.__format = 'hh:mm:ss'

        self.__timer = QTimer(self)
        self.__timer_interval = -1

        # init end time (00:00:00 by default)
        self.setEndHMS()

    def __initUi(self):
        self.setStartHMS()
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont('Arial', 24))

    def setTimerReverse(self, f: bool):
        if f:
            self.__timer_interval = -1
        else:
            self.__timer_interval = 1

    def setStartHMS(self):
        self.__startTime.setHMS(self.__start_hour, self.__start_min, self.__start_sec)
        time_left_text = self.__startTime.toString(self.__format)
        self.setText(time_left_text)

    def setEndHMS(self):
        self.__endTime.setHMS(self.__end_hour, self.__end_min, self.__end_sec)
        self.__end_text_time = self.__endTime.addSecs(-1).toString(self.__format)

    def setStartHour(self, h: int):
        self.__start_hour = h
        self.setStartHMS()

    def setStartMinute(self, m: int):
        self.__start_min = m
        self.setStartHMS()

    def setStartSecond(self, s: int):
        self.__start_sec = s
        self.setStartHMS()

    def setEndHour(self, h: int):
        self.__end_hour = h
        self.__setEndHMS()

    def setEndMinute(self, m: int):
        self.__end_min = m
        self.__setEndHMS()

    def setEndSecond(self, s: int):
        self.__end_sec = s
        self.__setEndHMS()

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
            time_left_text = self.__startTime.toString(self.__format)
            self.setText(time_left_text)
            if self.__end_text_time == time_left_text:
                self.__stop()
            else:
                pass
        except Exception as e:
            print(e)
            print(sys.exc_info()[2].tb_lineno)
            print(sys.exc_info())

    def stop(self):
        try:
            self.__startTime = QTime(self.__start_hour, self.__start_min, self.__start_sec)
            self.setText(self.__startTime.toString("hh:mm:ss"))

            self.__timer.stop()

            self.__timer.timeout.disconnect(self.__timerTicking)

        except Exception as e:
            print(e)
            print(sys.exc_info()[2].tb_lineno)
            print(sys.exc_info())

    def mouseDoubleClickEvent(self, e):
        self.doubleClicked.emit()
        return super().mouseDoubleClickEvent(e)
