# 메뉴바 만들기 https://wikidocs.net/21866

"""
한 개의 메뉴를 갖는 메뉴바를 만들었습니다.
이 메뉴는 클릭했을 때 어플리케이션을 종료하는 기능을 갖고 있습니다. 또한 이 기능은 단축키 (Ctrl+Q)로도 실행이 가능합니다.

"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')            # 단축키
        exitAction.setStatusTip('Exit application') # 상태바의 상태팁
        exitAction.triggered.connect(qApp.quit) 

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        """
        menuBar() 메서드는 메뉴바를 생성합니다. 이어서 'File' 메뉴를 하나 만들고, 거기에 'exitAction' 동작을 추가합니다.
        '&File'의 앰퍼샌드 (ampersand, &)는 간편하게 단축키를 설정하도록 해줍니다.
        'F' 앞에 앰퍼샌드가 있으므로 'Alt+F'가 File 메뉴의 단축키가 됩니다. 만약 'i'의 앞에 앰퍼샌드를 넣으면 'Alt+I'가 단축키가 됩니다.
        """

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())