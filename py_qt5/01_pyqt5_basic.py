# 창 띄우기

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My First Application") # 타이틀바에 나타나는 창의 제목
        self.move(300, 300)                         # 위젯 위치 설정
        self.resize(400, 200)                       # 위젯 크기, 너비, 높이 설정
        self.show()                                 # 위젯을 스크린에 띄움

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())