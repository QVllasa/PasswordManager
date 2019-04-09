import sys
from qtpy import QtWidgets, QtGui
from PyQt5.QtCore import *
from ui.mainwindow import Ui_MainWindow
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
import time
from selenium.webdriver.common.by import By
from accountLists import accounts, testAccounts

app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for key, value in testAccounts.items():
            self.ui.comboBox.addItem(key)

        browsers = ['Chrome', 'Firefox']
        self.ui.comboBox_2.addItems(browsers)

        self.currentBrowser = ''
        self.currentPassword = ''
        self.newPassword = ''
        self.accounts = ''

        self.ui.pushButton.clicked.connect(self.changePW)

    def changePW(self):
        self.currentBrowser = self.ui.comboBox_2.currentText()
        self.currentPassword = self.ui.inputCurrent.text()
        self.newPassword = self.ui.inputNew.text()
        self.accounts = self.ui.comboBox.currentText()
        self.obj = Worker(self.accounts, self.currentBrowser, self.currentPassword, self.newPassword)
        self.obj.message.connect(self.errorDialog)
        self.obj.finished.connect(self.done)
        self.obj.progress.connect(self.loadingBar)
        self.obj.label4.connect(self.okay4)
        self.obj.label5.connect(self.okay5)
        self.obj.start()

    def errorDialog(self, errorText):
        print(errorText)
        self.error_dialog = QtWidgets.QMessageBox()
        self.error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
        self.error_dialog.setText('Wrong Password in Account:' + errorText)

        self.error_dialog.show()

    def done(self, str):
        self.finish_dialog = QtWidgets.QMessageBox()
        self.finish_dialog.setIcon(QtWidgets.QMessageBox.Information)
        self.finish_dialog.setText('Passwords changed to:' + str)

    def loadingBar(self, percentage):
        print(percentage)
        self.ui.progressBar.setValue(percentage)

    def okay4(self):
        self.ui.label_4.setText('OK')

    def okay5(self):
        self.ui.label_5.setText('OK')



class Worker(QThread):
    message = pyqtSignal(str)
    finished = pyqtSignal(str)
    progress = pyqtSignal(float)
    label4 = pyqtSignal()
    label5 = pyqtSignal()

    def __init__(self, accounts, brwser, curPass, newPass):
        QThread.__init__(self)

        self.currentBrowser = brwser
        self.currentPassword = curPass
        self.newPassword = newPass
        self.accounts = accounts

    def run(self):
        count = float(0)
        while count < 100:
            for acc, address in testAccounts.items():
                if self.accounts == acc:
                    print(acc)
                    for user in testAccounts[acc]:
                        print(acc)
                        b = len(testAccounts[acc])
                        print(b)
                        if self.currentBrowser == 'Firefox':
                            count += 100 / b
                            page = "https://de.tradingview.com"
                            driver = webdriver.Firefox(executable_path="webdriver/geckodriver")
                            driver.implicitly_wait(30)
                            driver.minimize_window()
                            driver.get(page)
                            driver.find_element(By.XPATH, "(//a[contains(@href, '#signin')])[2]").click()
                            driver.find_element(By.NAME, "username").send_keys(user)
                            driver.find_element(By.NAME, "password").send_keys(self.currentPassword)
                            driver.find_element(By.XPATH,
                                                "//form[@id='signin-form']/div[3]/div[2]/button/span[2]").click()
                            try:
                                time.sleep(3)
                                driver.find_element(By.XPATH, "//div[4]/span/span").click()
                            except ElementNotInteractableException:
                                self.message.emit(user)
                                self.progress.emit(count)
                                driver.quit()
                                continue
                            self.label4 = pyqtSignal()
                            driver.find_element(By.XPATH,
                                                "//a[contains(@href, '/u/indaqub/#settings-profile')]").click()
                            driver.find_element(By.XPATH, "//fieldset[2]/span/span/span/span").click()
                            driver.find_element(By.XPATH,
                                                "//form[@id='change-password-form']/fieldset/span/span/div/input").click()
                            driver.find_element(By.NAME, "current_password").send_keys(self.currentPassword)
                            driver.find_element(By.ID, "id_password1").send_keys(self.newPassword)
                            driver.find_element(By.ID, "id_password2").send_keys(self.newPassword)
                            driver.find_element(By.XPATH,
                                                "//form[@id='change-password-form']/div/div/button/span[2]").click()
                            time.sleep(5)
                            driver.find_element(By.XPATH, "//div[4]/span/span").click()
                            driver.find_element(By.XPATH, "//a[contains(@href, '#signout')]").click()
                            self.label5 = pyqtSignal()
                            driver.quit()

                        self.progress.emit(count)
                        print(str(count) + '%')
        self.finished.emit(self.newPassword)


window = MainWindow()
window.show()

sys.exit(app.exec_())
