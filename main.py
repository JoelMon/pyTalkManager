#!/usr/bin/env python3

__author__ = 'Joel Montes de Oca'

from PySide import QtCore, QtGui
import sys

# Importation of custom mods
import pyTalkManager as TM

# Importation of GUIs
import gui.MainWindow


class MainWindow(QtGui.QMainWindow):


    """The main window of pyTalkManager."""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = gui.MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())