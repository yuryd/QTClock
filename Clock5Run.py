import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Clock5Run(QWidget):
    __WSep = 2
    __WX = __WY = 2
    def __init__(self, config, app, parent=None):
        super(Clock5Run, self).__init__(parent)
        self.__Config = config
        self.__App = app
        self.resize(200,200)
        self.setWindowTitle(self.__Config.Identification("Name"))
        self.labelName = QLabel(self)
        self.labelAuthor = QLabel(self)
        self.labelVersion = QLabel(self)
        self.labelName.setText(self.__Config.Identification("Name"))
        self.labelAuthor.setText(self.__Config.Identification("Author"))
        self.labelVersion.setText(f'{self.__Config.Identification("Version")["Major"]}.{self.__Config.Identification("Version")["Minor"]} {self.__Config.Identification("Version")["Status"]}')
        self.labelName.move(Clock5Run.__WX,Clock5Run.__WY)
        self.labelAuthor.move(Clock5Run.__WX,self.labelName.y()+self.labelName.height()+Clock5Run.__WSep)
        self.labelVersion.move(Clock5Run.__WX,self.labelAuthor.y()+self.labelAuthor.height()+Clock5Run.__WSep)

    def Run(self):
        self.show()
        sys.exit(self.__App.exec())
