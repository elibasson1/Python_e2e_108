from selenium.webdriver.common.by import By
from utillties.BaseClass import Base
from utillties import logging


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    ProductNumber = (By.XPATH, "//div[@class='card h-100']")

    def getProductNumber(self):  # products
        return self.driver.find_elements(*CheckOutPage.ProductNumber)

    Check_out_Button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def Check_out_Button1(self):
        self.driver.find_element(*CheckOutPage.Check_out_Button).click()

    CheckoutBtn_Sucsees = (By.XPATH, "//button[@class='btn btn-success']")

    def CheckoutBtnSucsees(self):
        self.driver.find_element(*CheckOutPage.CheckoutBtn_Sucsees).click()

    # --------------------------------------------------------------------------------

    # Not Done Yet

    find_specific_product = (By.XPATH, "div/h4")

    def find_specificProduct(self):  # products
        return self.driver.find_element(*CheckOutPage.find_specific_product)

    Selected_Product = (By.XPATH, "div[2]/button")

    def getProduct(self):  # products
        return self.driver.find_elements(*CheckOutPage.Selected_Product)

    def find_prod(self, All_products):
        log = logging.getlogger()

        for product in All_products:
            productName = product.find_element_by_xpath("div/h4").text
            log.info(productName)

            if productName == "Blackberry":
                product.find_element_by_xpath("div[2]/button").click()
