import pytest
from allure_commons._allure import title

from pages.LoginPage import LoginPage
from Config.config import TestData
from Tests.test_base import Basetest
from pages.HomePage import HomePage


class Test_HomePage(Basetest):

    @title("test homepage title")
    @pytest.fixture(scope='class')
    def test_homepage_title(self):
        global homePage
        self.loginPage = LoginPage(self.driver)
        homePage=self.loginPage.do_login(TestData.username, TestData.password)
        title = homePage.get_homepage_title("Swag Labs")
        assert title == "Swag Labs","invalid page title"
        print(title)

    @title("test page title of products page")
    @pytest.fixture(scope='class')

    def test_homepage_header(self,test_homepage_title):

        header=homePage.get_page_header()
        print(header)
        assert header=="Products","Invalid page header"

    @title("validate the products present in the cart")
    @pytest.fixture(scope='class')

    def test_homepage_products(self,test_homepage_title,test_homepage_header):

        product_title=homePage.get_product_titles()
        product_count = homePage.get_product_count()

        print(product_title)
        print(product_count)

        assert product_count == 6, "Product count on home page does not match expected value"

    @title("Validate add to cart button")

    def test_addcart_button(self,test_homepage_title,test_homepage_header,test_homepage_products):

        homePage.go_to_cart_page()








