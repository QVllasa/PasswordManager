# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AccDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
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
        self.verticalLayoutWidget = QtWidgets.QWidget(AccDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(AccDialog)
        self.buttonBox.accepted.connect(AccDialog.accept)
        self.buttonBox.rejected.connect(AccDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AccDialog)

    def retranslateUi(self, AccDialog):
        _translate = QtCore.QCoreApplication.translate
        AccDialog.setWindowTitle(_translate("AccDialog", "Show Accounts"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AccDialog", "Neue Spalte"))

