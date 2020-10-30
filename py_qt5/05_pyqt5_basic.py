# 상태바 만들기 https://wikidocs.net/21928

"""
메인창은 QMenuBar, QToolBar, QDockWidget, QStatusBar를 위한 고유의 레이아웃을 갖고 있습니다.
또한 가운데 영역에 중심위젯 (Central widget)을 위한 영역을 갖고 있습니다. 여기에는 어떠한 위젯도 들어올 수 있습니다.

QMainWindow 클래스를 이용해서 메인 어플리케이션 창을 만들 수 있습니다.

우선 QStatusBar를 이용해서 메인 창에 상태바 (status bar)를 하나 만든다.

상태바는 어플리케이션의 상태를 알려주기 위해 어플리케이션의 하단에 위치하는 위젯입니다.

상태바에 텍스트를 표시하기 위해서는 showMessage() 메서드를 사용합니다.
텍스트가 사라지게 하고 싶으면, clearMessage() 메서드를 사용하거나, showMessage() 메서드에 텍스트가 표시되는 시간을 설정할 수 있습니다.
현재 상태바에 표시되는 메세지 텍스트를 갖고 오고 싶을 때는 currentMessage() 메서드를 사용합니다.
QStatusBar 클래스는 상태바에 표시되는 메세지가 바뀔 때 마다 messageChanged() 시그널을 발생합니다.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        상태바는 QMainWindow 클래스의 statusBar() 메서드를 이용해서 만드는데, statusBar() 메서드를 최초로 호출함으로써 만들어집니다.
        그 다음 호출부터는 상태바 객체를 반환합니다.
        showMessage() 메서드를 통해 상태바에 보여질 메세지를 설정할 수 있습니다.
        """
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
