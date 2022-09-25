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

    __AmPmTimeFmt = [ ['%H:%M:%S','%I:%M:%S'], ['%H:%M','%I:%M'] ]
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
        timeFont = QFont('Arial', 24)
        dateFont = QFont('Arial', 12)
        self.labelName = QLabel(self)
        self.labelAuthor = QLabel(self)
        self.labelVersion = QLabel(self)
        self.labelALF = QLabel(self)
        self.labelALFText = QLabel(self)
        self.cb24hrClock = QCheckBox("24hr Clock")
        self.cbNoSeconds = QCheckBox("No Seconds")
        self.labelName.setText(self.__Config.Identification("Name"))
        self.labelAuthor.setText(self.__Config.Identification("Author"))
        self.labelVersion.setText(f'{self.__Config.Identification("Version")["Major"]}.{self.__Config.Identification("Version")["Minor"]} {self.__Config.Identification("Version")["Status"]}')
        self.labelALF.setText('ALF:')
        self.labelALFText.setText(self.__Config.ActivityListFile())
        self.labelDate = QLabel(self)
        self.labelTime = QLabel(self)
        self.labelAmPm = QLabel(self)
        self.labelLocation = QLabel(self)
        self.labelTimeCount = QLabel(self)
        self.labelTime.setAlignment(Qt.AlignCenter)
        self.labelDate.setAlignment(Qt.AlignCenter)
        self.labelTimeCount.setAlignment(Qt.AlignCenter)
        self.labelLocation.setAlignment(Qt.AlignCenter)
        self.labelDate.setFont(dateFont)
        self.labelTime.setFont(timeFont)
        self.labelAmPm.setFont(timeFont)
        self.labelLocation.setFont(timeFont)
        #self.labelTime.setStyleSheet("border: 1px solid black;")
        self.secondsTimer() # just to start the time display

        #Connect all widgets
        outerLayout = QVBoxLayout()
        headingLayout = QHBoxLayout()
        headingLayout.addWidget(self.labelName)
        headingLayout.addWidget(self.labelVersion)
        headingLayout.addWidget(self.labelAuthor)
        headingLayout.addStretch()
        headingLayout.addWidget(self.cb24hrClock)
        headingLayout.addWidget(self.cbNoSeconds)
        footingLayout = QHBoxLayout()
        footingLayout.addWidget(self.labelALF)
        footingLayout.addWidget(self.labelALFText)

        centreFrame = QFrame()
        centreFrame.setFrameShape(QFrame.StyledPanel)
        centreFrame.setLineWidth(1)

        centreLayout = QVBoxLayout()
        centreLayout1 = QHBoxLayout(centreFrame)
        centreLayout2 = QHBoxLayout()

        centreLayout1.addWidget(self.labelTime)
        centreLayout1.addWidget(self.labelAmPm)
        centreLayout2.addWidget(self.labelTimeCount)
        centreLayout.addWidget(self.labelDate)
        #centreLayout.addLayout(centreLayout1)
        centreLayout.addWidget(centreFrame)
        centreLayout.addLayout(centreLayout2)
        centreLayout.addWidget(self.labelLocation)
        outerLayout.addLayout(headingLayout)
        outerLayout.addLayout(centreLayout)
        outerLayout.addLayout(footingLayout)
        self.centralWidget.setLayout(outerLayout)

        #Create timer
        timeTimer = QTimer(self)
        timeTimer.setInterval(1000)
        timeTimer.timeout.connect(self.secondsTimer)
        timeTimer.start()


    def Run(self):
        self.show()
        sys.exit(self.__App.exec())

    def secondsTimer(self):
        #colon = Clock5Run.__Colons[self.__TimeCount % 2]
        colon = Clock5Run.__ColonList[self.__ColCnt]
        self.colCount()
        self.__TimeCount += 1
        now = datetime.datetime.now()
        nowDate = now.strftime('%b %d, %Y')
        nowTime = now.strftime(Clock5Run.__AmPmTimeFmt[self.IsNoSeconds()][self.Is24hrClock()])
        nowAmPm = now.strftime('%p')
        self.labelDate.setText(f'{nowDate}')
        self.labelTime.setText(f'{nowTime}')
        self.labelAmPm.setText(f'{nowAmPm}' if not(self.Is24hrClock()) else f'')
        self.labelTimeCount.setText(f'{colon}{self.__TimeCount}{colon}')
        #self.labelTime.adjustSize()
        self.labelDate.adjustSize()
        self.labelTimeCount.adjustSize()

    def colCount(self):
        if self.__ColCntDir == 1:
            (self.__ColCnt, self.__ColCntDir) = (Clock5Run.__MaxVal - 1, -1) if self.__ColCnt == Clock5Run.__MaxVal else (self.__ColCnt + 1, self.__ColCntDir)
        else:
            (self.__ColCnt, self.__ColCntDir) = (1, 1) if self.__ColCnt == 0 else (self.__ColCnt - 1, self.__ColCntDir)

    def Is24hrClock(self):
        return self.cb24hrClock.isChecked()

    def IsNoSeconds(self):  
        return self.cbNoSeconds.isChecked()
