# QCalendarWidget : https://wikidocs.net/33771

"""
QCalendarWidget을 이용해서 사용자가 날짜를 선택할 수 있도록 달력을 표시할 수 있습니다.

달력은 월 단위로 표시되고, 처음 실행될 때 현재의 연도, 월, 날짜로 선택되어 있습니다.

자세한 내용은 QCalendarWidget 공식 문서에서 확인할 수 있습니다.

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        """
        QCalenderWidget의 객체(cal)를 하나 만듭니다.

        setGridVisible(True)로 설정하면, 날짜 사이에 그리드가 표시됩니다.

        날짜를 클릭했을 때 showDate 메서드가 호출되도록 연결해줍니다.

        """

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())
        # showDate 메서드에서, 날짜를 클릭할 때마다 라벨 텍스트가 선택한 날짜(date.toString())로 표시되도록 합니다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())