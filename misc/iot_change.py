from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

page = "https://academy2.eu1.mindsphere.io/index.html#/"
driver = webdriver.Firefox(
    executable_path='webdriver/macOS/geckodriver')

driver.implicitly_wait(3)
# driver.minimize_window()
driver.get(page)

driver.find_element(By.XPATH, "//fieldset[@id='dr_signin']/div[2]/div/input").send_keys('qendrim.vllasa@siemens.com')
time.sleep(1)
driver.find_element(By.XPATH, "//fieldset[@id='dr_signin']/div[3]/div/input").send_keys('Dominim123_=')
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='login-button']").click()
time.sleep(3)
driver.find_element(By.XPATH,
                    "//div[@id='_mscontent']/mindsphere-app-root/div/mindsphere-launchpad-container/div/div/div/div[6]/div/mindsphere-launchpad-tile-container/a/div").click()

driver.find_element(By.XPATH, "(//input[@name='user'])[2]").send_keys('qendrim.vllasa@siemens.com')

driver.find_element(By.XPATH, "(//input[@name='password'])[2]").send_keys('Dominim123_2')

driver.find_element(By.XPATH, "(//button[@type='submit'])[5]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='app']/div/c8y-ui-header/div/div/div[3]/button/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[@id='app']/div/c8y-ui-header/div/div/div[3]/ul/li/a").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[9]/button/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys('Dominim123_3')
driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys('Dominim123_3')
time.sleep(3)
driver.find_element(By.XPATH, "//div[3]/button[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='currentPassword']").send_keys('Dominim123_2')
driver.find_element(By.XPATH, "//button").click()
driver.delete_all_cookies()
driver.quit()
