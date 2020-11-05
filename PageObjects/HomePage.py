from selenium.webdriver.common.by import By
from utillties.BaseClass import Base


class HomePgae:

    def __init__(self, driver):
        self.driver = driver

    def load_url(self):
        self.driver.maximize_window()
        self.driver.get("https://www.rahulshettyacademy.com/angularpractice/")

    shop = (By.CSS_SELECTOR, "a[href='/angularpractice/shop']")

    def shopItem(self):
        self.driver.find_element(*HomePgae.shop).click()

#  --------------------------------------------------------------

    name1 = (By.NAME, "name")

    def myname(self):
        return self.driver.find_element(*HomePgae.name1)

    email = (By.NAME, "email")

    def enter_my_email(self):
        return self.driver.find_element(*HomePgae.email)

    exampleCheck1 = (By.ID, "exampleCheck1")

    def example_Check1(self):
        self.driver.find_element(*HomePgae.exampleCheck1).click()

    list = (By.ID, "exampleFormControlSelect1")

    def list_box(self):
        return self.driver.find_element(*HomePgae.list)

    btnsuccess = (By.CSS_SELECTOR, "input[class='btn btn-success']")

    def btn_success(self):
        self.driver.find_element(*HomePgae.btnsuccess).click()

