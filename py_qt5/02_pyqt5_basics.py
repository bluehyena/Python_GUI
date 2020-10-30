# 어플리케이션 아이콘 넣기

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')
        
        # setWindowIcon() 매서드, 어플리케이션 아이콘 설정
        # QIcon 객체 생성, QIcon()에 보여질 이미지 입력 web.png
        # 이미지 파일이 다른 디렉토리에 있는경우 경로입력.
        self.setWindowIcon(QIcon('web.png'))
        
        # setGeometry() 메서드는 창의 위치와 크기 설정
        # 창의 x, y 위치 창의 너비, 높이 를 각각 설정함
        # 01의 move()와 resize()를 합친 메서드.  
        self.setGeometry(300, 300, 300, 200)
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())