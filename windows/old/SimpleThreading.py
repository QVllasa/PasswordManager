import sys
from qtpy import QtWidgets, QtGui
from PyQt5.QtCore import *
from macOS.ui.mainwindow import Ui_MainWindow
import time

app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.changePW)


    def done(self):
        QtGui.QMessageBox.information(self, "Done!", "Done fetching posts!")



    def changePW(self):

        self.obj = Worker()
        self.obj.signal.connect(self.obj.signal, pyqtSignal('finished()'), self.done)
        self.obj.start()
        #print('ende:'+obj.error)

    def errorDialog(self):
        print('hi from thread')
        # print('errorDialog starten...')
        # self.msg = QtWidgets.QDialog()
        # self.msg.exec_()


class Worker(QThread):

    def __init__(self):
        QThread.__init__(self)

        #add a signal
        self.signal = pyqtSignal(int)



    def run(self, value):
        time.sleep(5)


    def handle_signal(self):
        self.signal.emit('wrong password')




window = MainWindow()
window.show()

sys.exit(app.exec_())
