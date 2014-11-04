#!/usr/bin/env python3

__author__ = 'Joel Montes de Oca'

from PySide.QtCore import *
from PySide.QtGui import *
import sys

# Importation of custom mods
import pyTalkManagerDatabase as DB
import pyTalkManager as TM

# Importation of GUIs
import main


def main():

    firstrun = TM.configGet('APP', 'FirstTimeRunning')





if __name__ == '__main__':
    main()
