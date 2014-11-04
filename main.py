#!/usr/bin/env python3

__author__ = 'Joel Montes de Oca'

import sys
from PySide import QtGui
import pyTalkManagerDatabase as DB
import pyTalkManager as TM


def main():

    firstrun = TM.configGet('APP', 'FirstTimeRunning')
    app = QtGui.QApplication(sys.argv)

    wid = QtGui.QWidget()
    wid.resize(250, 150)
    wid.setWindowTitle('pyTalkManager')
    wid.show()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
