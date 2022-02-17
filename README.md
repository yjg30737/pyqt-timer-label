# pyqt-timer-label
PyQt QLabel for timer feature

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-timer-label.git --upgrade```

## Detailed Description
You can set start hour/min/sec. Same to end. You can use this when you want to make a timer label which follows ```hh:mm:ss``` format.

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

Result

https://user-images.githubusercontent.com/55078043/154182901-bb7fd5fb-4eb1-46dd-bd5e-3cc9bacf95c7.mp4

Note: I started recording from 12 seconds approximately. Preparation for recording took time so the result shows from the moment which indicates 9 seconds left.

## See Also
* <a href="https://github.com/yjg30737/pyqt-timer.git">pyqt-timer</a>
* <a href="https://github.com/yjg30737/pyqt-transparent-timer.git">pyqt-transparent-timer</a>
