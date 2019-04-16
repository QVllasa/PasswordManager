from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC 
import time


# create a new Firefox session
driver = webdriver.Firefox(executable_path="/Users/qendrimvllasa/geckodriver") #choose either firefox or chrome webdriver location
driver.implicitly_wait(30)
driver.maximize_window()



connetivityAccounts = []
developerAccounts = []
intrductionAccounts = []



# Navigate to the application home page


# #change password
driver.find_element(By.XPATH, "(//a[contains(@href, '#signin')])[2]").click()

driver.find_element(By.NAME, "username").send_keys("indaqub")
driver.find_element(By.NAME, "password").send_keys("Dominim123_321")

driver.find_element(By.XPATH, "//form[@id='signin-form']/div[3]/div[2]/button/span[2]").click()

time.sleep(3)

driver.find_element(By.XPATH, "//div[4]/span/span").click()

driver.find_element(By.XPATH, "//a[contains(@href, '/u/indaqub/#settings-profile')]").click()

driver.find_element(By.XPATH, "//fieldset[2]/span/span/span/span").click()

driver.find_element(By.XPATH, "//form[@id='change-password-form']/fieldset/span/span/div/input").click()

driver.find_element(By.NAME, "current_password").send_keys("Dominim123_321")

driver.find_element(By.ID, "id_password1").send_keys("Dominim123_!")

driver.find_element(By.ID, "id_password2").send_keys("Dominim123_!")

driver.find_element(By.XPATH, "//form[@id='change-password-form']/div/div/button/span[2]").click()

time.sleep(3)

driver.find_element(By.XPATH, "//div[4]/span/span").click()

driver.find_element(By.XPATH, "//a[contains(@href, '#signout')]").click()




#driver.close()