from pathlib import Path
import shutil

firefox_webdriver = Path('webdriver/geckodriver')

chrome_webdriver = Path('webdriver/chromedriver')

#testing
#destinationF = Path('/Users/qendrimvllasa/Desktop/geckodriver')
#destinationC = Path('/Users/qendrimvllasa/Desktop/chromedriver')

destinationF = Path('/usr/local/bin/geckodriver')
destinationC = Path('/usr/local/bin/chromedriver')


def copyWebDriver():
    if not destinationF.exists():
        shutil.copy(firefox_webdriver, destinationF)
    else:
        print('ff in desktop')

    if not destinationC.exists():
        shutil.copy(chrome_webdriver, destinationC)
    else:
        print('cc in desktop')


copyWebDriver()
