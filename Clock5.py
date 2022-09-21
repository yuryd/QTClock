from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Clock5Run
import Config

class ClockRun(object):
    def __init__(self, config):
        self.__Config = config

    def __enter__(self):
        app = QApplication([])
        self.__Clock5 = Clock5Run.Clock5Run(self.__Config, app)
        return self.__Clock5

    def __exit__(self, type, value, traceback):
        pass
        #print(type, value, traceback)

def main():
    config = Config.Config()
    #clock5 = Clock5Run.Clock5Run(Config)
    with ClockRun(config) as clock:
        clock.Run()

if __name__ == '__main__':
    main()
