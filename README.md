# pyqt-timer-label
PyQt QLabel adapted to timer feature

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-timer-label`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-responsive-label.git">pyqt-responsive-label</a> - for auto-resize the font of label accordance with window's size 

## Detailed Description
You can set start hour/min/sec. Same to end. You can use this when you want to make a timer label which follows ```hh:mm:ss``` format. By the way, default end time is 00:00:00. You can change it with methods i'll explain below.

## Method, Signal Overview
* ```setStartHour(h: int)```, ```setStartMinute(m: int)```, ```setStartSecond(s: int)```. Same to end.
* ```setTimerReverse(f: bool)``` to make timer go reversed. Default is True, which means subtracts one second.
* There are useful methods like ```start()```, ```pause()```, ```restart()```, ```refresh()```, ```reset()```, ```stop()``` as well as useful signals like ```doubleClicked```, ```prepared```, ```started```, ```paused```, ```restarted```, ```refreshed```, ```resetSignal```, ```stopped```.
* `isPaused() -> bool` - Check if the timer being paused or not

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from pyqt_timer_label import TimerLabel


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    lbl = TimerLabel()
    lbl.setStartHour(0)
    lbl.setStartMinute(0)
    lbl.setStartSecond(15)
    widget = QWidget()
    lay = QGridLayout()
    lay.addWidget(lbl)
    widget.setLayout(lay)
    widget.show()
    lbl.start()
    sys.exit(app.exec_())
```
Start time is 00:00:15. End time is by default so it is 00:00:00. 

Result

https://user-images.githubusercontent.com/55078043/154182901-bb7fd5fb-4eb1-46dd-bd5e-3cc9bacf95c7.mp4

Note: I started recording from 12 seconds approximately. Preparation for recording took time so the result shows from the moment which indicates 9 seconds left.

## See Also
* <a href="https://github.com/yjg30737/pyqt-timer.git">pyqt-timer</a>
* <a href="https://github.com/yjg30737/pyqt-transparent-timer.git">pyqt-transparent-timer</a>
