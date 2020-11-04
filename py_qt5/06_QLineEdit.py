# QLineEdit : https://wikidocs.net/33806

"""
QLineEdit은 한 줄의 문자열을 입력하고 수정할 수 있도록 하는 위젯입니다.

QLineEdit.Normal	            0	입력된 문자를 표시합니다. (기본값)
QLineEdit.NoEcho	            1	문자열을 표시하지 않습니다. 이 설정은 비밀번호의 글자수도 공개하지 않을 때 유용합니다.
QLineEdit.Password	            2	입력된 문자 대신 비밀번호 가림용 문자를 표시합니다.
QLineEdit.PasswordEchoOnEdit	3	입력할 때만 문자를 표시하고, 수정 중에는 다른 문자를 표시합니다.

시그널
cursorPositionChanged()	        커서가 움직일 때 발생하는 신호를 발생합니다.
editingFinished()	            편집이 끝났을 때 (Return/Enter 버튼이 눌릴 때) 신호를 발생합니다.
returnPressed()	Return/Enter    버튼이 눌릴 때 신호를 발생합니다.
selectionChanged()	            선택 영역이 바뀔 때 신호를 발생합니다.
textChanged()	                텍스트가 변경될 때 신호를 발생합니다.
textEdited()	                텍스트가 편집될 때 신호를 발생합니다.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        qle = QLineEdit(self)
        qle.move(60, 100)
        qle.textChanged[str].connect(self.onChanged)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())