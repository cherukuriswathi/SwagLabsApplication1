import time

import pytest
from allure_commons._allure import title

from Config.config import TestData
from Tests.test_base import Basetest
from pages.LoginPage import LoginPage


class Test_CartPage(Basetest):

    @title(" validate cart page and products present in the cart ")
    @pytest.fixture(scope='class')
    def test_products_in_cart(self):
        global cartPage
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.username, TestData.password)
        cartPage = homePage.go_to_cart_page()
        product_names = cartPage.get_cart_product_titles()
        product_count = cartPage.get_cart_product_count()
        print(product_names)
        assert len(product_names) == product_count,f'incorrect count of products present in the cart:{product_count}'


    @title(" validate checkout button's text")
    def test_checkout_button_text(self,test_products_in_cart):
        checkout_text = cartPage.get_checkout_text()
        assert checkout_text == "Checkout", f'Checkout button text is invalid:{checkout_text}'
        print(checkout_text)












