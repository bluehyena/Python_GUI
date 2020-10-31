# 툴바 만들기 https://wikidocs.net/21932

"""
메뉴(menu)가 어플리케이션에서 사용되는 모든 명령의 모음이라면
툴바(toolbar)는 자주 사용하는 명령들을 더 편리하게 사용할 수 있도록 해줍니다.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        메뉴바의 경우와 마찬가지로 QAction 객체를 하나 생성합니다.
        이 객체는 아이콘 (exit.png), 라벨 ('Exit')을 포함하고, 단축키 (Ctrl+Q)를 통해 실행 가능합니다.
        상태바에 메세지 ('Exit application')를 보여주고, 클릭 시 생성되는 시그널은 quit() 메서드에 연결되어 있습니다.

        """
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')            # 단축키
        exitAction.setStatusTip('Exit application') # 상태바의 상태팁
        exitAction.triggered.connect(qApp.quit) 
        
        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())