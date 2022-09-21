import sys
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Clock5Run(QMainWindow):
    __WSep = 2
    __WX = __WY = 2
    def __init__(self, config, app, parent=None):
        super().__init__()
        self.__Config = config
        self.__App = app
        self.__Count = 0
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
        centreLayout = QHBoxLayout()
        centreLayout.addWidget(self.labelTime)
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
        time = QDateTime.currentDateTime()
        self.labelTime.setText(f'{time}')
