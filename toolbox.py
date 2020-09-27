"""
Handy functions to produce test data.
"""

import random
from string import ascii_letters
import scribe


class Toolbox:

    log = scribe.customLogger()

    def getuniquename(self):
        listofnames = ['Randy', 'Butters', 'Kenny', 'Stan', 'Eric']
        listoflastnames = ['Marsh', 'Cartman', 'Mccortmic', 'Mckey', 'Smith']
        randomperson = ''.join(random.choice(listofnames).lower() + random.choice(listoflastnames).lower())
        return randomperson

    def getuniqueemail(self):
        uniquename = self.getuniquename()
        return uniquename + "@mail.com"

    def getuniquepassword(self):
        randomchars = ''.join([random.choice(ascii_letters) for i in range(1, 5)])
        randomnums = str(random.randint(299, 1999))
        return randomchars + randomnums + '#'

    def verifyTextContains(self, actualText, expectedText):

        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAIN !!!")
            return False
