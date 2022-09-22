import sys
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Clock5Run(QMainWindow):
    __WSep = 2
    __WX = __WY = 2
    __Colons = [':', ' ']
    __ColonList = [ ':'*10,
            ':'*9,
            ':'*8,
            ':'*7,
            ':'*6,
            ':'*5,
            ':'*4,
            ':'*3,
            ':'*2,
            ':'*1]
    __MaxVal = len(__ColonList) - 1
    def __init__(self, config, app, parent=None):
        super().__init__()
        self.__Config = config
        self.__App = app
        self.__Count = 0
        self.__TimeCount = 0
        self.__ColCnt = 0
        self.__ColCntDir = 1
        self.setupUI()

    def newWindowTitle(self):
        self.__Count += 1
        self.setWindowTitle(f'{self.__Config.Identification("Name")} {self.__Count}')

    def setupUI(self):
        self.resize(200,200)
        #self.setWindowTitle(self.__Config.Identification("Name"))
        self.newWindowTitle()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        #Create all widgets
        timeFont = QFont('Arial', 16)
        self.labelName = QLabel(self)
        self.labelAuthor = QLabel(self)
        self.labelVersion = QLabel(self)
        self.labelALF = QLabel(self)
        self.labelALFText = QLabel(self)
        self.pushButton = QPushButton("Press me!")
        self.pushButton.clicked.connect(self.buttonPressed)
        self.labelName.setText(self.__Config.Identification("Name"))
        self.labelAuthor.setText(self.__Config.Identification("Author"))
        self.labelVersion.setText(f'{self.__Config.Identification("Version")["Major"]}.{self.__Config.Identification("Version")["Minor"]} {self.__Config.Identification("Version")["Status"]}')
        self.labelALF.setText('ALF:')
        self.labelALFText.setText(self.__Config.ActivityListFile())
        self.labelTime = QLabel(self)
        self.labelTimeCount = QLabel(self)
        self.labelTimeCount.setAlignment(Qt.AlignCenter)
        self.labelTime.setFont(timeFont)
        self.secondsTimer() # just to start the time display

        #Connect all widgets
        outerLayout = QVBoxLayout()
        headingLayout = QHBoxLayout()
        headingLayout.addWidget(self.labelName)
        headingLayout.addWidget(self.labelVersion)
        headingLayout.addWidget(self.labelAuthor)
        headingLayout.addStretch()
        headingLayout.addWidget(self.pushButton)
        footingLayout = QHBoxLayout()
        footingLayout.addWidget(self.labelALF)
        footingLayout.addWidget(self.labelALFText)
        centreLayout = QVBoxLayout()
        centreLayout2 = QHBoxLayout()
        centreLayout.addWidget(self.labelTime)
        centreLayout2.addWidget(self.labelTimeCount)
        centreLayout.addLayout(centreLayout2)
        outerLayout.addLayout(headingLayout)
        outerLayout.addLayout(centreLayout)
        outerLayout.addLayout(footingLayout)
        self.centralWidget.setLayout(outerLayout)

        #Create timer
        timeTimer = QTimer(self)
        timeTimer.setInterval(1000)
        timeTimer.timeout.connect(self.secondsTimer)
        timeTimer.start()


    def buttonPressed(self):
        self.newWindowTitle()

    def Run(self):
        self.show()
        sys.exit(self.__App.exec())

    def secondsTimer(self):
        #colon = Clock5Run.__Colons[self.__TimeCount % 2]
        colon = Clock5Run.__ColonList[self.__ColCnt]
        self.colCount()
        self.__TimeCount += 1
        now = datetime.datetime.now().strftime('%b %d, %Y %H:%M:%S')
        self.labelTime.setText(f'{now}')
        self.labelTimeCount.setText(f'{colon}{self.__TimeCount}{colon}')

    def colCount(self):
        if self.__ColCntDir == 1:
            (self.__ColCnt, self.__ColCntDir) = (Clock5Run.__MaxVal - 1, -1) if self.__ColCnt == Clock5Run.__MaxVal else (self.__ColCnt + 1, self.__ColCntDir)
        else:
            (self.__ColCnt, self.__ColCntDir) = (1, 1) if self.__ColCnt == 0 else (self.__ColCnt - 1, self.__ColCntDir)
