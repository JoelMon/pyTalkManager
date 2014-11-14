# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/BrotherWindow.ui'
#
# Created: Fri Nov 14 11:10:11 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BrotherWindow(object):
    def setupUi(self, BrotherWindow):
        BrotherWindow.setObjectName("BrotherWindow")
        BrotherWindow.resize(578, 330)
        self.gridLayout = QtGui.QGridLayout(BrotherWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtGui.QFrame(BrotherWindow)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.button_close = QtGui.QPushButton(self.frame)
        self.button_close.setObjectName("button_close")
        self.horizontalLayout_2.addWidget(self.button_close)
        self.button_ok = QtGui.QPushButton(self.frame)
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout_2.addWidget(self.button_ok)
        self.gridLayout.addWidget(self.frame, 4, 1, 1, 1)
        self.frame_2 = QtGui.QFrame(BrotherWindow)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.button_delete = QtGui.QPushButton(self.frame_2)
        self.button_delete.setObjectName("button_delete")
        self.horizontalLayout.addWidget(self.button_delete)
        self.button_add = QtGui.QPushButton(self.frame_2)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout.addWidget(self.button_add)
        self.button_edit = QtGui.QPushButton(self.frame_2)
        self.button_edit.setObjectName("button_edit")
        self.horizontalLayout.addWidget(self.button_edit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addWidget(self.frame_2, 3, 1, 1, 1)
        self.tableView = QtGui.QTableView(BrotherWindow)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 1, 2, 2)

        self.retranslateUi(BrotherWindow)
        QtCore.QObject.connect(self.button_close, QtCore.SIGNAL("clicked()"), BrotherWindow.close)
        QtCore.QMetaObject.connectSlotsByName(BrotherWindow)

    def retranslateUi(self, BrotherWindow):
        BrotherWindow.setWindowTitle(QtGui.QApplication.translate("BrotherWindow", "Brothers", None, QtGui.QApplication.UnicodeUTF8))
        self.button_close.setText(QtGui.QApplication.translate("BrotherWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.button_ok.setText(QtGui.QApplication.translate("BrotherWindow", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete.setText(QtGui.QApplication.translate("BrotherWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.button_add.setText(QtGui.QApplication.translate("BrotherWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.button_edit.setText(QtGui.QApplication.translate("BrotherWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))

