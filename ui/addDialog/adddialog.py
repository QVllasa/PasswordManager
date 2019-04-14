# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/addDialog\adddialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addDialog(object):
    def setupUi(self, addDialog):
        addDialog.setObjectName("addDialog")
        addDialog.resize(274, 351)
        self.okButton = QtWidgets.QPushButton(addDialog)
        self.okButton.setGeometry(QtCore.QRect(20, 310, 75, 23))
        self.okButton.setObjectName("okButton")
        self.quitButton = QtWidgets.QPushButton(addDialog)
        self.quitButton.setGeometry(QtCore.QRect(180, 310, 75, 23))
        self.quitButton.setObjectName("quitButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(addDialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 80, 231, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.listName = QtWidgets.QLineEdit(addDialog)
        self.listName.setGeometry(QtCore.QRect(20, 30, 231, 20))
        self.listName.setObjectName("listName")
        self.label = QtWidgets.QLabel(addDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 47, 13))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(addDialog)
        QtCore.QMetaObject.connectSlotsByName(addDialog)

    def retranslateUi(self, addDialog):
        _translate = QtCore.QCoreApplication.translate
        addDialog.setWindowTitle(_translate("addDialog", "addDialog"))
        self.okButton.setText(_translate("addDialog", "OK"))
        self.quitButton.setText(_translate("addDialog", "Quit"))
        self.label.setText(_translate("addDialog", "List Name"))
        self.label_2.setText(_translate("addDialog", "Accounts"))


