# QSlider & QDial : https://wikidocs.net/21942

"""
상수	                값	                설명
QSlider.NoTicks     	0	    틱을 표시하지 않습니다.
QSlider.TicksAbove     	1	    틱을 (수평) 슬라이더 위쪽에 표시합니다.
QSlider.TicksBelow	    2	    틱을 (수평) 슬라이더 아래쪽에 표시합니다.
QSlider.TicksBothSides	3	    틱을 (수평) 슬라이더 양쪽에 표시합니다.
QSlider.TicksLeft	TicksAbove	틱을 (수직) 슬라이더 왼쪽에 표시합니다.
QSlider.TicksRight	TicksBelow	틱을 (수직) 슬라이더 오른쪽에 표시합니다.
"""

"""
시그널:
valueChanged()	슬라이더의 값이 변할 때 발생합니다.
sliderPressed()	사용자가 슬라이더를 움직이기 시작할 때 발생합니다.
sliderMoved()	사용자가 슬라이더를 움직이면 발생합니다.
sliderReleased()	사용자가 슬라이더를 놓을 때 발생합니다.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self) # Qslider 위젯 생성
        self.slider.move(30, 30)
        self.slider.setRange(0, 50) # setRange()로 메서드 값의 범위를 0에서 50으로 설정.
        self.slider.setSingleStep(2)

        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)

        btn = QPushButton('Default', self)
        btn.move(35, 160)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked) # 'Default' 푸시 버튼을 클릭하면 발생하는 시그널을 button_clicked 메서드에 연결합니다.

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def button_clicked(self):
        """
        button_clicked() 메서드는 슬라이더와 다이얼의 값을 모두 0으로 조절합니다.

        따라서 'Default' 푸시 버튼을 클릭하면, 슬라이더와 다이얼의 값이 0으로 초기화됩니다.
        """
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())