import pytest
# import inspect
# import logging
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Base:

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    # def getlogger(self):
    #     loggername = inspect.stack()[1][3]
    #     logger = logging.getLogger(loggername)  # __import__()  --> for test case name
    #     fileHandler = logging.FileHandler('logfile.log')  # create file to save all log file
    #     formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    #     fileHandler.setFormatter(formatter)
    #     logger.addHandler(fileHandler)  # file handler object
    #     logger.setLevel(logging.DEBUG)
    #     return logger
