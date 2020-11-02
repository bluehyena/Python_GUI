# Qcheckbox : https://wikidocs.net/21937
"""
QCheckBox 위젯은 on(체크됨)/off(체크안됨)의 두 상태를 갖는 버튼을 제공합니다. 이 위젯은 하나의 텍스트 라벨과 함께 체크 박스를 제공합니다. (QCheckBox 공식 문서 참고)


체크 박스가 선택되거나 해제될 때, stateChanged() 시그널을 발생합니다. 체크 박스의 상태가 변할 때마다 어떠한 동작을 발생시키고 싶을 때, 이 시그널을 특정 슬롯에 연결할 수 있습니다.


또한 체크 박스의 선택 여부를 확인하기 위해서, isChecked() 메서드를 사용할 수 있습니다. 선택 여부에 따라 boolean 값을 반환합니다.
"""

"""
자주 쓰이는 메서드 :
text()	체크 박스의 라벨 텍스트를 반환합니다.
setText()	체크 박스의 라벨 텍스트를 설정합니다.
isChecked()	체크 박스의 상태를 반환합니다. (True/False)
checkState()	체크 박스의 상태를 반환합니다. (2/1/0)
toggle()	체크 박스의 상태를 변경합니다.
"""

"""
자주 쓰이는 시그널 :
pressed()	체크 박스를 누를 때 신호를 발생합니다.
released()	체크 박스에서 뗄 때 신호를 발생합니다.
clicked()	체크 박스를 클릭할 때 신호를 발생합니다.
stateChanged()	체크 박스의 상태가 바뀔 때 신호를 발생합니다.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show Title', self) # 'Show title'이라는 텍스트 라벨을 갖는 체크박스를 하나 만듭니다.
        cb.move(20, 20)
        cb.toggle() # 체크박스는 디폴트로 체크가 되어있지 않은 off 상태로 나타나기 때문에 on 상태로 바꾸기 위해 toggle() 메서드를 사용했습니다.
        cb.stateChanged.connect(self.changeTitle) # 체크박스의 상태가 바뀔 때 발생하는 시그널 (stateChanged)을 우리가 정의한 changeTitle() 메서드에 연결합니다.

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
        """
        체크박스의 상태 (state)가 changeTitle() 메서드의 매개변수로 주어집니다.

        체크가 되어있으면 타이틀을 'QCheckBox'로, 그렇지 않으면 빈 문자열로 나타내게 됩니다.
        """
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())