import sys
from qtpy.QtWidgets import *
from PyQt5.QtCore import *
from ui.mainwindow import Ui_MainWindow
from ui.Dialog import Ui_Dialog
from ui.AccDialog import Ui_AccDialog
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from accountLists import accounts
from docx import Document
import datetime

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.testing = ''

        self.currentBrowser = ''
        self.currentPassword = ''
        self.newPassword = ''
        self.accounts = ''

        self.finish_dialog = QMessageBox()
        self.error_dialog = QMessageBox()
        self.docx_dialog = QMessageBox()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for key, value in accounts.items():
            self.ui.comboBox.addItem(key)

        browsers = ['Chrome', 'Firefox']
        self.ui.comboBox_2.addItems(browsers)

        self.ui.label_5.hide()
        self.ui.label_4.hide()

        self.ui.pushButton.clicked.connect(self.changePW)

        # self.ui.add.clicked.connect(self.addList)

        self.ui.showAccBtn.clicked.connect(self.showAcc)

    def changePW(self):
        self.currentBrowser = self.ui.comboBox_2.currentText()
        self.currentPassword = self.ui.inputCurrent.text()
        self.newPassword = self.ui.inputNew.text()
        self.accounts = self.ui.comboBox.currentText()
        self.obj = Worker(self.accounts, self.currentBrowser, self.currentPassword, self.newPassword)
        self.obj.message.connect(self.errorDialog)
        self.obj.finished.connect(self.done)
        self.obj.progress.connect(self.loadingBar)
        self.obj.docFinish.connect(self.docxDialog)
        self.obj.label4.connect(self.okay4)
        self.obj.label5.connect(self.okay5)
        self.obj.start()

    # TODO
    # def addList(self):
    #     dialog = QDialog()
    #     ui = Ui_Dialog()
    #     ui.setupUi(dialog)
    #     dialog.show()
    #     rsp = dialog.exec_()
    #     if rsp == QDialog.Accepted:
    #         if ui.listName.text():
    #             print(ui.listName.text())
    #
    #         for i in range(0, ui.accTable.rowCount()):
    #             if ui.accTable.item(i, 0):
    #                 print(ui.accTable.item(i, 0).text())
    #     else:
    #         print('Cancel')

    # TODO
    def showAcc(self):
        dialog = QDialog()
        ui = Ui_AccDialog()
        ui.setupUi(dialog)
        for key in accounts:
            ui.comboBox.addItem(key)
            for value in accounts[key]:
                ui.listWidget.addItem(value)

        dialog.show()
        dialog.exec_()

    def errorDialog(self, errorText):
        print(errorText)
        self.error_dialog.setIcon(QMessageBox.Critical)
        self.error_dialog.setText('Wrong Password in Account:' + errorText)
        self.error_dialog.show()

    def done(self, str):
        self.finish_dialog.setIcon(QMessageBox.Information)
        self.finish_dialog.setText('Passwords changed to:   ' + str)
        self.finish_dialog.show()

    def loadingBar(self, percentage):
        print(percentage)
        self.ui.progressBar.setValue(percentage)

    def docxDialog(self, str):
        self.docx_dialog.setIcon(QMessageBox.Information)
        self.docx_dialog.setText(str)
        self.docx_dialog.show()

    def okay4(self, okay1):
        self.ui.label_4.setText(okay1)
        self.ui.label_4.show()

    def okay5(self, okay2):
        self.ui.label_5.setText(okay2)
        self.ui.label_5.show()


class Worker(QThread):
    message = pyqtSignal(str)
    finished = pyqtSignal(str)
    progress = pyqtSignal(float)
    label4 = pyqtSignal(str)
    label5 = pyqtSignal(str)
    docFinish = pyqtSignal(str)

    def __init__(self, accounts, brwser, curPass, newPass):
        QThread.__init__(self)

        self.currentBrowser = brwser
        self.currentPassword = curPass
        self.newPassword = newPass
        self.accounts = accounts

    def run(self):
        document = Document()

        table = document.add_table(rows=1, cols=2)
        document.add_paragraph(str(datetime.datetime.now()))
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'User Account'
        hdr_cells[1].text = 'Password (also for IoT Ext. and Integration)'

        count = float(0)
        self.progress.emit(count)
        while count < 100:
            for acc, address in accounts.items():
                if self.accounts == acc:
                    print(acc)
                    for user in accounts[acc]:
                        print(acc)
                        b = len(accounts[acc])
                        print(b)
                        if self.currentBrowser == 'Firefox':
                            count += 100 / b
                            page = "https://www2.industrysoftware.automation.siemens.com/webkey/"
                            options = webdriver.FirefoxOptions()
                            # options.add_argument('-headless')
                            driver = webdriver.Firefox(executable_path='webdriver/macOS/geckodriver', options=options)
                            driver.implicitly_wait(30)
                            # driver.minimize_window()
                            driver.get(page)

                            # time.sleep(4)
                            driver.find_element(By.XPATH, "//tr[5]/td[2]/ul/font/li/a/font").click()

                            # time.sleep(4)
                            driver.find_element(By.XPATH, "//td[2]/input").click()
                            driver.find_element(By.NAME, "WebKey_Username").send_keys(user)
                            driver.find_element(By.NAME, "Existing_WebKey_Password").send_keys(self.currentPassword)
                            driver.find_element(By.NAME, "pass").click()
                            driver.find_element(By.NAME, "pass").send_keys(self.newPassword)
                            driver.find_element(By.NAME, "repass").click()
                            driver.find_element(By.NAME, "repass").send_keys(self.newPassword)

                            driver.find_element(By.XPATH, "//div[3]/div[2]/div/form/fieldset/input").click()
                            time.sleep(3)

                            if driver.find_element(By.XPATH, "//h2[contains(.,'WebKey Error')]"):
                                self.message.emit(user)
                                self.progress.emit(count)
                                row_cells = table.add_row().cells
                                row_cells[0].text = user
                                row_cells[1].text = 'Wrong Password entered!'
                                empty_cells = table.add_row().cells
                                empty_cells[0].text = ''
                                empty_cells[1].text = ''
                                driver.quit()
                                continue

                            #if driver.find_element(By.XPATH, ):

                            #if driver.find_element(By.XPATH, ):


                            # except NoSuchElementException:
                            #     self.message.emit(user)
                            #     self.progress.emit(count)
                            #     row_cells = table.add_row().cells
                            #     row_cells[0].text = user
                            #     row_cells[1].text = 'Wrong Password entered!'
                            #     empty_cells = table.add_row().cells
                            #     empty_cells[0].text = ''
                            #     empty_cells[1].text = ''
                            #     driver.quit()
                            #     continue

                            self.label4.emit('OK')
                            self.label5.emit('OK')
                            driver.quit()

                            row_cells = table.add_row().cells
                            row_cells[0].text = user
                            row_cells[1].text = self.newPassword
                            empty_cells = table.add_row().cells
                            empty_cells[0].text = ''
                            empty_cells[1].text = ''

                        self.progress.emit(count)
                        print(str(count) + '%')
        self.finished.emit(self.newPassword)
        for acc in accounts:
            if acc == self.accounts:
                document.save(acc + '.docx')
        self.docFinish.emit('Word file with all changed accounts created and saved in application folder! :)')


window = MainWindow()
window.show()

sys.exit(app.exec_())
