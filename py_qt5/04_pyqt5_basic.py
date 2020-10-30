# 툴팁 나타내기
# 툴팁은 어떤 위젯의 기능을 설명하는 등의 역할을 하는 말풍선 형태의 도움말

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10)) # 10px 크기의 'SansSerif' 폰트를 사용
        self.setToolTip('This is a <b>QWidget</b> widget') # setToolTip() 메서드를 사용해서, 표시될 텍스트를 입력

        btn = QPushButton('Button', self)   # 버튼을 만들고 툴팁을 달아준다.
        self.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint()) # sizeHint() 버튼을 적절한 크기로 설정

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())