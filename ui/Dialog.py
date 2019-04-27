# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.listName.setObjectName("listName")
        self.verticalLayout.addWidget(self.listName)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.accTable = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.accTable.setObjectName("accTable")
        self.accTable.setColumnCount(1)
        self.accTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.accTable.setHorizontalHeaderItem(0, item)
        self.accTable.horizontalHeader().setVisible(False)
        self.accTable.horizontalHeader().setStretchLastSection(True)
        self.accTable.verticalHeader().setVisible(False)
        self.accTable.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.accTable)
        self.addRow = QtWidgets.QPushButton(Dialog)
        self.addRow.setGeometry(QtCore.QRect(280, 110, 113, 32))
        self.addRow.setObjectName("addRow")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Accounts"))
        self.label.setText(_translate("Dialog", "List Name"))
        self.label_2.setText(_translate("Dialog", "Accounts"))
        item = self.accTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Neue Spalte"))
        self.addRow.setText(_translate("Dialog", "Add Row"))

