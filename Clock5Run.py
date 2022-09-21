import sys
from PyQt5.QtCore import *
from pyQt5.QtGui import *
from pyQt5.QtWidgets import *

class Clock5Run(QWidget):
    def __init__(self, config, parent=None):
        super(window, self).__init__(parent)
        self.__Config = config
        self.resize(200,200)
        self.setWindowTitle(self.__Config.Identification("Name"))
        self.labelName = QLabel(self)
        self.labelAuthor = QLabel(self)
        self.labelVersion = QLabel(self)
        self.labelname = self.__Config.Identification("Name")
        self.labelAuthor = self.__Config.Identification("Author")
        self.labelVersion = f'{self.__Config.Identification("Version")["Major"]}.{self.__Config.Identification("Version")["Minor"]} {self.__Config.Identification("Version")["Status"]}'
        self.labelName.move(10,10)
        self.labelAuthor.move(10,50)
        self.labelVersion.move(10,90)

    def Run(self):
        pass
