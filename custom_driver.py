from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import scribe
import logging
import time
import os


class CustomDriver:
    log = scribe.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def takeScreenshot(self, resultMessage):
        """
        Takes screenshot of the entire page and names it after the logged message
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:

            self.driver.save_screenshot(destinationDirectory)
            self.log.info("Screenshot was saved to directory: " + destinationFile)
        except:
            self.log.error(":: !!!! Exception Occurred while taking a screenshot:: !!!! ")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self, typeOfLocator):
        typeOfLocator = typeOfLocator.lower()
        if typeOfLocator == "id":
            return By.ID
        elif typeOfLocator == "name":
            return By.NAME
        elif typeOfLocator == "xpath":
            return By.XPATH
        elif typeOfLocator == "css":
            return By.CSS_SELECTOR
        elif typeOfLocator == "class":
            return By.CLASS_NAME
        elif typeOfLocator == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + typeOfLocator +
                          " not correct/supported")
        return False

    def getElement(self, locator, typeOfLocator="xpath"):
        element = None
        try:
            typeOfLocator = typeOfLocator.lower()
            byType = self.getByType(typeOfLocator)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with the locator: " + locator +
                          " and typeOfLocator was: " + typeOfLocator)
        except:
            self.log.info("Element not found with the locator: " + locator +
                          " and typeOfLocator was: " + typeOfLocator)
        return element

    def elementClick(self, locator, typeOfLocator="xpath"):
        try:
            element = self.getElement(locator, typeOfLocator)
            element.click()
            self.log.info("Clicked on the element with the locator: " + locator +
                          " typeOfLocator: " + typeOfLocator)
        except:
            self.log.info("Cannot click on the element with the locator: " + locator +
                          " typeOfLocator: " + typeOfLocator)
            print_stack()

    def sendKeys(self, message, locator, typeOfLocator="id"):
        try:
            element = self.getElement(locator, typeOfLocator)
            element.send_keys(message)
            self.log.info("Sent the message to the element with the locator: " + locator +
                          " typeOfLocator: " + typeOfLocator)
        except:
            self.log.info("Could not send the message to the element with locator: " + locator +
                          " locatorType: " + typeOfLocator)
            print_stack()

    def isElementPresent(self, locator, typeOfLocator="xpath"):
        try:
            element = self.getElement(locator, typeOfLocator)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + typeOfLocator)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + typeOfLocator)
                return False
        except:
            print("Element not found")
            return False

    def elementsPresenceCheck(self, locator, typeOfLocator):
        try:
            elementList = self.driver.find_elements(typeOfLocator, locator)
            if len(elementList) > 0:
                self.log.info("Elements are present with locator: " + locator +
                              " locatorType: " + str(typeOfLocator))
                return True
            else:
                self.log.info("Elements are not present with locator: " + locator +
                              " locatorType: " + str(typeOfLocator))
                return False
        except:
            self.log.info("There are no elements with such locator")
            return False

    def waitForElement(self, locator, locatorType="xpath",
                       timeout=10):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            self.log.info("Waiting for :: " + str(timeout) +
                          " :: seconds for element to be clickable and timeout")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(element))
            self.log.info("The element is present on the web page")
        except:
            self.log.info("Element is not present on the web page")
            print_stack()
        return element
