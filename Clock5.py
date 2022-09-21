import PyQT5.QTCore import *
import PyQt5.QtGui import *
import PyQt5.QtWidgets import *

import Clock5Run
import Config

class ClockRun(object):
    def __init__(self, config):
        self.__Config = config

    def __enter__(self):
        app = QApplication(self.__Config.Identification("Name"))
        self.__Clock5 = Clock5Run.Clock5Run(self.__Config)
        self.__Clock5.Run(app)

    def __exit__(self):
        pass

def main():
    config = Config.Config()
    clock5 = Clock5Run.Clock5Run(Config)
    clock5.Run()

if __name__ == '__main__':
    main()
