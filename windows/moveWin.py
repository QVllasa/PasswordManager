from pathlib import Path
import shutil

firefox_webdriver = Path('webdriver/geckodriver.exe')

chrome_webdriver = Path('webdriver/chromedriver.exe')

#testing
#destinationF = Path('/Users/qendrimvllasa/Desktop/geckodriver')
#destinationC = Path('/Users/qendrimvllasa/Desktop/chromedriver')

destinationF = Path('C:/Windows/System32/geckodriver.exe')
#destinationC = Path('C:/Windows/System32/chromedriver')


def copyWebDriver():
    if not destinationF.exists():
        shutil.copy(firefox_webdriver, destinationF)
    else:
        print('ff in desktop')

    #if not destinationC.exists():
     #   shutil.copy(chrome_webdriver, destinationC)
    #else:
     #   print('cc in desktop')


#copyWebDriver()
