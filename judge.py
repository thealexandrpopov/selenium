"""
Takes in a custom result message and asserts test result (PASS or FAIL)
"""

import scribe
import logging
from custom_driver import CustomDriver
from traceback import print_stack


class AssertStatus(CustomDriver):
    log = scribe.customLogger(logging.INFO)

    def __init__(self, driver):
        super(AssertStatus, self).__init__(driver)
        self.listOfResults = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.listOfResults.append("PASS")
                    self.log.info(":: PASSED VERIFICATION :: + " + resultMessage)
                else:
                    self.listOfResults.append("FAIL")
                    self.log.error(":: FAILED VERIFICATION :: + " + resultMessage)
                    self.takeScreenshot(resultMessage)
            else:
                self.listOfResults.append("FAIL")
                self.log.error(":: FAILED VERIFICATION :: + " + resultMessage)
                self.takeScreenshot(resultMessage)
        except:
            self.listOfResults.append("FAIL")
            self.log.error(":: !!! Exception Occurred !!! ::")
            self.takeScreenshot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        """
        Marks the result of verification in one test case.
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Marks the final result of the verification point in a test case
        Final test status of the test case. Returns True if there are 0 failures in the test.
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.listOfResults:
            self.log.error(testName + ":: TEST FAILED ::")
            self.listOfResults.clear()
            assert True == False
        else:
            self.log.info(testName + ":: TEST PASSED ::")
            self.listOfResults.clear()
            assert True == True
