from PyQt5 import QtCore, QtGui, QtWidgets
from ui.addDialog.adddialog import Ui_addDialog

class addDialog(QtWidgets.QInputDialog):
    def __init__(self):



        self.ui = Ui_addDialog()
        self.ui.setupUi(self)

        #self.app = QtWidgets.QDialog(sys.argv)

        #sys.exit(self.app.exec_())

    def pop(self):
        self.ui.show()