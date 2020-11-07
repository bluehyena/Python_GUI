# QTapWidget : https://wikidocs.net/33707

"""
GUI 프로그램을 사용하다보면 위의 그림과 같이 탭(Tab)이 있는 창을 볼 수 있습니다.

이러한 탭은 프로그램 안의 구성요소들이 많은 면적을 차지하지 않으면서, 그것들을 카테고리에 따라 분류할 수 있기 때문에 유용하게 사용될 수 있습니다.

간단한 예제를 통해 두 개의 탭을 갖는 위젯을 하나 만들어보겠습니다.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
305163
51056
    def initUI(self):
        tab1 = QWidget()
        tab2 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())