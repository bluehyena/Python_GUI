# 날짜와 시간 표시 : https://wikidocs.net/22074
"""
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QDateTime

time = QTime.currentTime()
now = QDate.currentDate()
datetime = QDateTime.currentDateTime()

print(time.toString())
print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('ddd.MMMM.yyyy'))
# print(now.toString(Qt.ISODate)) 
# print(now.toString(Qt.DefaultLocaleLongDate))

print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString('hh.mm.ss.zzz')) # 'h'는 시간(hour), 'm'은 분(minute), 's'는 초(second), 그리고 'z'는 1000분의 1초를 나타냅니다.
# print(time.toString(Qt.DefaultLocaleLongDate))
# print(time.toString(Qt.DefaultLocaleShortDate))
 
print(datetime.toString('d.M.yy hh:mm:ss'))
print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
# print(datetime.toString(Qt.DefaultLocaleLongDate))
# print(datetime.toString(Qt.DefaultLocaleShortDate))
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())