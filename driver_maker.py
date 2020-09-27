"""
Takes in browser parameter, sets up the driver, implicit wait, maximizes window, opens the base url and returns driver.
"""

from selenium import webdriver


class DriverMaker:

    def __init__(self, browser):

        self.browser = browser

    def getWebDriverInstance(self):

        baseURL = "http://miralova.com.fozzyhost.com/"

        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        driver.implicitly_wait(3)

        driver.maximize_window()

        driver.get(baseURL)

        return driver
