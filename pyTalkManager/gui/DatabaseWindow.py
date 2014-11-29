# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatabaseWindow.ui'
#
# Created: Fri Nov  7 21:02:42 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DatabaseWindow(object):
    def setupUi(self, DatabaseWindow):
        DatabaseWindow.setObjectName("DatabaseWindow")
        DatabaseWindow.resize(144, 128)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DatabaseWindow.sizePolicy().hasHeightForWidth())
        DatabaseWindow.setSizePolicy(sizePolicy)
        DatabaseWindow.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(DatabaseWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtGui.QPushButton(DatabaseWindow)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(DatabaseWindow)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(DatabaseWindow)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)

        self.retranslateUi(DatabaseWindow)
        QtCore.QMetaObject.connectSlotsByName(DatabaseWindow)

    def retranslateUi(self, DatabaseWindow):
        DatabaseWindow.setWindowTitle(QtGui.QApplication.translate("DatabaseWindow", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setToolTip(QtGui.QApplication.translate("DatabaseWindow", "Load a backup.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("DatabaseWindow", "Load Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("DatabaseWindow", "Create a new database.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("DatabaseWindow", "New Database", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setToolTip(QtGui.QApplication.translate("DatabaseWindow", "Backup your data.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("DatabaseWindow", "Backup", None, QtGui.QApplication.UnicodeUTF8))

