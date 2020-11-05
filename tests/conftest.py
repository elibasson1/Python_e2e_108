import pytest
from pyvirtualdisplay import Display
from selenium import webdriver
from xvfbwrapper import Xvfb
driver = None


# Pass different values to a test function, depending on command line options
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


# Fixture for browser - chrome and firefox
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browserName = request.config.getoption("browser_name")
    if browserName == "firefox":
        driver = webdriver.Firefox(executable_path="/home/eli/Documents/SelniumDriver/geckodriver")
    elif browserName == "chrome":
        vdisplay = Xvfb()
        vdisplay.start()

        display = Display(visible=0, size=(1920, 1080))
        display.start()

        driver = webdriver.Chrome("/home/eli/Documents/SelniumDriver/chromedriver")

    # driver.maximize_window()
    # driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()