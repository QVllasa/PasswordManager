import sys
from selenium import webdriver
from selenium.webdriver.common.by import By


currentPassword = 'Dominim123_321'
newPassword = 'Dominim123_!'
user = 'indaqub'

page = "https://de.tradingview.com"
print(currentPassword)
print(newPassword)
print('starting firefox')
driver = webdriver.Firefox(executable_path="webdriver/geckodriver")
driver.implicitly_wait(30)
driver.minimize_window()
print('open firefox')
driver.get(page)
print('load: ' + page)
driver.find_element(By.XPATH, "(//a[contains(@href, '#signin')])[2]").click()
print('clicked on signin')
driver.find_element(By.NAME, "username").send_keys(user)
print('entered username: ' + user)
driver.find_element(By.NAME, "password").send_keys(currentPassword)
print('password entered: ' + currentPassword)
driver.find_element(By.XPATH,
                    "//form[@id='signin-form']/div[3]/div[2]/button/span[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[4]/span/span").click()

driver.find_element(By.XPATH,
                    "//a[contains(@href, '/u/indaqub/#settings-profile')]").click()
driver.find_element(By.XPATH, "//fieldset[2]/span/span/span/span").click()
driver.find_element(By.XPATH,
                    "//form[@id='change-password-form']/fieldset/span/span/div/input").click()
driver.find_element(By.NAME, "current_password").send_keys(currentPassword)
driver.find_element(By.ID, "id_password1").send_keys(newPassword)
driver.find_element(By.ID, "id_password2").send_keys(newPassword)
driver.find_element(By.XPATH,
                    "//form[@id='change-password-form']/div/div/button/span[2]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[4]/span/span").click()
driver.find_element(By.XPATH, "//a[contains(@href, '#signout')]").click()
driver.quit()
print('password changed to' + newPassword)