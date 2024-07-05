import pytest
from allure_commons._allure import title

from Config.config import TestData
from Tests.test_base import Basetest
from pages.LoginPage import LoginPage

class Test_Overview_page(Basetest):

    @title(" validate overview page ")
    @pytest.fixture(scope='class')
    def test_overview_page_title (self):
        global overviewPage
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.username, TestData.password)
        cartPage = homePage.go_to_cart_page()
        checkout_Page = cartPage.click_checkout_button()
        checkout_Page.get_your_information_page(TestData.firstname, TestData.lastname, TestData.postalcode)
        overviewPage = checkout_Page.click_continue()
        overview_title = overviewPage.get_page_header()
        print(overview_title)
        assert overview_title == "Checkout: Overview", f'overview page title is incorrect{overview_title}'

    @title("validate the finish button ")
    def test_finish_button(self,test_overview_page_title):

        finsh_text=overviewPage.get_finish_text()
        assert finsh_text == "Finish", f'finish button text is incorrect{finsh_text}'
        overviewPage.click_finish_button()




