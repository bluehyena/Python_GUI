# 그리드 레이아웃 : https://wikidocs.net/21946

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout() # QGridLayout을 만들고, 어플리케이션 창의 레이아웃으로 설정합니다.
        self.setLayout(grid)
        """
        addWidget() 메서드의 첫 번째 위젯은 추가할 위젯, 두, 세 번째 위젯은 각각 행과 열 번호를 입력합니다.
        세 개의 라벨을 첫 번째 열에 수직으로 배치합니다.
        """
        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1) # QTextEdit() 위젯은 QLineEdit() 위젯과 달리 여러 줄의 텍스트를 수정할 수 있는 위젯입니다. 세 번째 행, 두 번째 열에 배치합니다.

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())        