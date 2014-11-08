#!/usr/bin/env python3

import pyTalkManager as TM
from PySide import QtCore, QtGui
import sys

# Importation of GUIs
import gui.MainWindow
import gui.DatabaseWindow


def main():

    first_run = TM.configGet('APP', 'FirstTimeRunning')


class MainWindow(QtGui.QMainWindow, gui.MainWindow.Ui_MainWindow):


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # Tool bar actions
        self.actionDatabase.triggered.connect(self.show_database_dialog)


    def show_database_dialog(self):
        self.dbwindow = DatabaseWindow()
        self.dbwindow.show()


class DatabaseWindow(QtGui.QDialog, gui.DatabaseWindow.Ui_DatabaseWindow):
  def __init__(self, parent=None):
    super(DatabaseWindow, self).__init__(parent)
    self.setupUi(self)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my_app = MainWindow()
    my_app.show()
    sys.exit(app.exec_())
