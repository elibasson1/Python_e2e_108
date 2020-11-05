from selenium.webdriver.common.by import By

from utillties.BaseClass import Base


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    Select_Cuntry = (By.ID, "country")

    def SelectCuntry(self):
        return self.driver.find_element(*ConfirmPage.Select_Cuntry)

    Click_On_Select_Cuntry = (By.LINK_TEXT, "India")

    def ClickOn_Select_Cuntry(self):
        self.driver.find_element(*ConfirmPage.Click_On_Select_Cuntry).click()

    click_on_check_box = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")

    def clickonCheck_box(self):
        self.driver.find_element(*ConfirmPage.click_on_check_box).click()

    Purchase_click = (By.CSS_SELECTOR, "input[value='Purchase']")

    def PurchaseClick(self):
        self.driver.find_element(*ConfirmPage.Purchase_click).click()

    SuccessText = (By.CSS_SELECTOR , "div[class*='alert-success']")

    def Success_Text(self):
        return self.driver.find_element(*ConfirmPage.SuccessText).text
