# QGroupBox : https://wikidocs.net/32153

"""
그룹 박스는 상단 타이틀과 단축키 (shortcut)를 제공하며, 그 안에 다양한 위젯들을 나타낼 수 있습니다. (QGroupBox 공식 문서 참고)

QGroupBox 클래스는 제목과 제목의 정렬을 설정하도록 해줍니다. 그룹 박스는 체크 가능하도록 설정할 수 있는데, 그룹 박스의 체크 여부에 따라 그 그룹 박스 안에 있는 위젯들이 사용 가능하거나 불가능해집니다.

공간을 절약하기 위해 flat 속성을 활성화할 수 있는데, 보통 프레임의 왼쪽, 오른쪽, 아래쪽 가장자리가 없게 표됩니다.
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton
, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)

        self.setLayout(grid)

        self.setWindowTitle('항공권 비교 분석기')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox('항공권의 종류를 선택하세요')

        radio1 = QRadioButton('편도')
        radio2 = QRadioButton('왕복')
        radio3 = QRadioButton('다구간')
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox

    def createSecondExclusiveGroup(self):
        groupbox = QGroupBox('왕복일 경우 체크 해주세요')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)
        checkbox = QCheckBox('Independent Checkbox')
        checkbox.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkbox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createNonExclusiveGroup(self):
        groupbox = QGroupBox('Non-Exclusive Checkboxes')
        groupbox.setFlat(True)

        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)
        tristatebox = QCheckBox('Tri-state Button')
        tristatebox.setTristate(True)

        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(tristatebox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createPushButtonGroup(self):
        groupbox = QGroupBox('Push Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(True)

        pushbutton = QPushButton('Normal Button')
        togglebutton = QPushButton('Toggle Button')
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)
        flatbutton = QPushButton('Flat Button')
        flatbutton.setFlat(True)
        popupbutton = QPushButton('Popup Button')
        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        popupbutton.setMenu(menu)

        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(togglebutton)
        vbox.addWidget(flatbutton)
        vbox.addWidget(popupbutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())