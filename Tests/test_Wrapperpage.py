import pytest
from allure_commons._allure import title
from Config.config import TestData
from Tests.test_base import Basetest
from pages.LoginPage import LoginPage


class Test_WrapperPage(Basetest):

    @title("to validate the wrap/end page of the application and validate back home button")
    @pytest.fixture(scope='class')
    def test_Wrap_page_title(self):
        global pageWrap
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.username, TestData.password)
        cartPage = homePage.go_to_cart_page()
        checkout_Page = cartPage.click_checkout_button()
        checkout_Page.get_your_information_page(TestData.firstname, TestData.lastname, TestData.postalcode)
        overviewPage = checkout_Page.click_continue()
        pageWrap = overviewPage.click_finish_button()
        text = pageWrap.get_page_header()
        assert text == "Checkout: Complete!",f'page header is incorrect{text}'
        print(text)

    @title("validate the page text")
    @pytest.fixture(scope='class')
    def test_page_text(self, test_Wrap_page_title):

        page_text=pageWrap.get_wrapper_text()

        assert page_text == "Thank you for your order!",f'page text is incorrect{page_text}'
        print(page_text)

    @title("validate back home button")
    def test_back_home_button(self, test_Wrap_page_title, test_page_text):
        back_home_text=pageWrap.get_back_home_text()
        print(back_home_text)
        assert back_home_text == "Back Home",f'back home button text is incorrect{back_home_text}'

        pageWrap.click_back_home()












