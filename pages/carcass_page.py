"""
Must be inherited by all pages, contains methods that are common across all pages.
"""
from custom_driver import CustomDriver
from traceback import print_stack
from toolbox import Toolbox


class CarcassPage(CustomDriver):

    def __init__(self, driver):

        super(CarcassPage, self).__init__(driver)
        self.driver = driver
        self.tool = Toolbox()

    def verifyPageTitle(self, titleToVerify):
        """
        Compares the given title with the title of the current page.
        """
        try:
            actualTitle = self.getTitle()
            return self.tool.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
