import pytest

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePgae
from TestData.HomePageData import HomePageData
from utillties.BaseClass import Base
from utillties import logging


class TestOne(Base):
    def test_e2e(self, getData):
        log = logging.getlogger()
        log.info("get home page")
        homepage = HomePgae(self.driver)
        homepage.load_url()
        homepage.myname().send_keys(getData["firstName"])  # Send Send Values from dictionary Option 1
        homepage.enter_my_email().send_keys(getData["lastName"])  # Send Send Values from dictionary Option 1
        # homepage.myname().send_keys(getData[0])  # Send Values from tuple Option 2
        # homepage.enter_my_email().send_keys(getData[1])  # Send Values from tuple Option 2
        homepage.example_Check1()
        self.selectOptionByText(homepage.list_box(), getData["Gender"])  # Send Send Values from dictionary Option 1
        # self.selectOptionByText(homepage.list_box(), getData[2])  # Send Values from tuple Option 2
        homepage.btn_success()
        homepage.shopItem()

        Check_Out_Page = CheckOutPage(self.driver)
        All_products = Check_Out_Page.getProductNumber()
        Check_Out_Page.find_prod(All_products)
        Check_Out_Page.Check_out_Button1()
        Check_Out_Page.CheckoutBtnSucsees()
#
#       ProtoCommerce Page - IND Page
        confirm_page = ConfirmPage(self.driver)
        confirm_page.SelectCuntry().send_keys("ind")
        self.verifyLinkPresence("India")  # take from Baas class
        confirm_page.ClickOn_Select_Cuntry()
        confirm_page.clickonCheck_box()
        confirm_page.PurchaseClick()
        SuccessText = confirm_page.Success_Text()
        assert "Success! Thank you!" in SuccessText
        self.driver.refresh()
#       driver.get_screenshot_as_file("screen.png")


#  Option 1 Send Send Values from dictionary
@pytest.fixture(params=HomePageData.test_HomePage_Data)
def getData(request):
    return request.param


# Option 2  Send Values from tuple
# @pytest.fixture(params=[("Eli-1", "Basson-1@gmail.com", "Female"), ("Eli-2", "Basson-2@gmail.com", "Male")])
# def getData(request):
#     return request.param