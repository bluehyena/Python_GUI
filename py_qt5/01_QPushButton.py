# QPushButton : https://wikidocs.net/21934

"""
메서드:
setCheckable()	True 설정 시, 누른 상태와 그렇지 않은 상태를 구분합니다.
toggle()	    상태를 바꿉니다.
setIcon()	    버튼의 아이콘을 설정합니다.
setEnabled()	False 설정 시, 버튼을 사용할 수 없습니다.
isChecked()	    버튼의 선택 여부를 반환합니다.
setText()   	버튼에 표시될 텍스트를 설정합니다.
text()	        버튼에 표시된 텍스트를 반환합니다.

시그널:
clicked()	    버튼을 클릭할 때 발생합니다.
pressed()	    버튼이 눌렸을 때 발생합니다.
released()	    버튼을 눌렀다 뗄 때 발생합니다.
toggled()	    버튼의 상태가 바뀔 때 발생합니다.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        QPushButton 클래스로 푸시 버튼을 하나 만듭니다. 첫 번째 파라미터로는 버튼에 나타날 텍스트, 두 번째는 버튼이 속할 부모 클래스를 지정해줍니다.

        버튼에 단축키(shortcut)를 지정하고 싶으면 아래와 같이 해당 문자 앞에 ampersand('&')를 넣어주면 됩니다. 이 버튼의 단축키는 'Alt+b'가 됩니다.

        setCheckable()을 True로 설정해주면, 선택되거나 선택되지 않은 상태를 유지할 수 있게 됩니다.

        toggle() 메서드를 호출하면 버튼의 상태가 바뀌게 됩니다. 따라서 이 버튼은 프로그램이 시작될 때 선택되어 있습니다.

        """
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False) # setEnabled()를 False로 설정하면, 버튼을 사용할 수 없게 됩니다.

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())