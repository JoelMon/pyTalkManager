# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CongregationWindow.ui'
#
# Created: Sun Nov 16 20:08:17 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CongregationWindow(object):
    def setupUi(self, CongregationWindow):
        CongregationWindow.setObjectName("CongregationWindow")
        CongregationWindow.resize(565, 347)
        CongregationWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        CongregationWindow.setSizeGripEnabled(True)
        CongregationWindow.setModal(False)
        self.gridLayout = QtGui.QGridLayout(CongregationWindow)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtGui.QFrame(CongregationWindow)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
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
        self.gridLayout.addWidget(self.frame, 3, 1, 1, 1)
        self.frame_2 = QtGui.QFrame(CongregationWindow)
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(6, 6, -1, 6)
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
        self.gridLayout.addWidget(self.frame_2, 2, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(CongregationWindow)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 1, 1)

        self.retranslateUi(CongregationWindow)
        QtCore.QObject.connect(self.button_close, QtCore.SIGNAL("clicked()"), CongregationWindow.close)
        QtCore.QMetaObject.connectSlotsByName(CongregationWindow)

    def retranslateUi(self, CongregationWindow):
        CongregationWindow.setWindowTitle(QtGui.QApplication.translate("CongregationWindow", "Congregations", None, QtGui.QApplication.UnicodeUTF8))
        self.button_close.setText(QtGui.QApplication.translate("CongregationWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.button_ok.setText(QtGui.QApplication.translate("CongregationWindow", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete.setText(QtGui.QApplication.translate("CongregationWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.button_add.setText(QtGui.QApplication.translate("CongregationWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.button_edit.setText(QtGui.QApplication.translate("CongregationWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))

