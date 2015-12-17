# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddOutlineWindow.ui'
#
# Created: Tue May 19 18:14:27 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddOutlineWindow(object):
    def setupUi(self, AddOutlineWindow):
        AddOutlineWindow.setObjectName("AddOutlineWindow")
        AddOutlineWindow.resize(424, 140)
        self.gridLayout_2 = QtGui.QGridLayout(AddOutlineWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_cancel = QtGui.QPushButton(AddOutlineWindow)
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout_2.addWidget(self.button_cancel, 2, 1, 1, 1)
        self.button_save = QtGui.QPushButton(AddOutlineWindow)
        self.button_save.setObjectName("button_save")
        self.gridLayout_2.addWidget(self.button_save, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.frame = QtGui.QFrame(AddOutlineWindow)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line_number = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_number.sizePolicy().hasHeightForWidth())
        self.line_number.setSizePolicy(sizePolicy)
        self.line_number.setMinimumSize(QtCore.QSize(10, 0))
        self.line_number.setObjectName("line_number")
        self.gridLayout.addWidget(self.line_number, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.line_title = QtGui.QLineEdit(self.frame)
        self.line_title.setObjectName("line_title")
        self.gridLayout.addWidget(self.line_title, 2, 1, 1, 2)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 3)

        self.retranslateUi(AddOutlineWindow)
        QtCore.QObject.connect(self.button_cancel, QtCore.SIGNAL("clicked()"), AddOutlineWindow.close)
        QtCore.QMetaObject.connectSlotsByName(AddOutlineWindow)

    def retranslateUi(self, AddOutlineWindow):
        AddOutlineWindow.setWindowTitle(QtGui.QApplication.translate("AddOutlineWindow", "Add an Outline", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel.setText(QtGui.QApplication.translate("AddOutlineWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save.setText(QtGui.QApplication.translate("AddOutlineWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddOutlineWindow", "Outline title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddOutlineWindow", "Outline number:", None, QtGui.QApplication.UnicodeUTF8))

