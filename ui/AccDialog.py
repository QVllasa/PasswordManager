# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AccDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AccDialog(object):
    def setupUi(self, AccDialog):
        AccDialog.setObjectName("AccDialog")
        AccDialog.resize(461, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(AccDialog)
        self.buttonBox.setGeometry(QtCore.QRect(360, 10, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listView = QtWidgets.QListView(AccDialog)
        self.listView.setGeometry(QtCore.QRect(30, 60, 301, 192))
        self.listView.setObjectName("listView")
        self.comboBox = QtWidgets.QComboBox(AccDialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 311, 32))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(AccDialog)
        self.buttonBox.accepted.connect(AccDialog.accept)
        self.buttonBox.rejected.connect(AccDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AccDialog)

    def retranslateUi(self, AccDialog):
        _translate = QtCore.QCoreApplication.translate
        AccDialog.setWindowTitle(_translate("AccDialog", "AccDialog"))


