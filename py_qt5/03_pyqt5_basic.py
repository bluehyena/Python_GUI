# 창 닫기

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("Quit", self) # 푸시버튼 생성, (버튼에 표시될 텍스트, 버튼이 위치할 부모 위젯)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        # PyQt5에서의 이벤트 처리는 시그널과 슬롯 메커니즘으로 이루어집니다.
        # 버튼 (btn)을 클릭하면 'clicked' 시그널이 만들어집니다.
        # instance() 메서드는 현재 인스턴스를 반환합니다.
        # 'clicked' 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결됩니다.
        # 이렇게 발신자 (Sender)와 수신자 (Receiver), 두 객체 간에 커뮤니케이션이 이루어집니다.
        # 이 예제에서 발신자는 푸시버튼 (btn)이고, 수신자는 어플리케이션 객체 (app)입니다.
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())