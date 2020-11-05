from selenium import webdriver
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome("/home/eli/Documents/SelniumDriver/chromedriver")
# driver.maximize_window()
# driver.get("https://www.rahulshettyacademy.com/angularpractice/")
#
# driver.find_element_by_name("name").send_keys("eli")
# driver.find_element_by_name("email").send_keys("eli@gmail.com")
# driver.find_element_by_id("exampleCheck1").click()
#
# select = Select(driver.find_element_by_id("exampleFormControlSelect1"))
# select.select_by_visible_text("Female")
# driver.find_element_by_css_selector("input[class='btn btn-success']").click()


class Base:
    driver = webdriver.Chrome("/home/eli/Documents/SelniumDriver/chromedriver")
    y = 5


class Protractor(Base):
    def startpage(self):
        self.driver.maximize_window()
        self.driver.get("https://www.rahulshettyacademy.com/angularpractice/")


x = Protractor()
x.startpage()