import os

import allure
import pytest
from allure_commons._allure import title

from Config.config import TestData
from Tests.test_base import Basetest
from pages.LoginPage import LoginPage


class Test_checkout_page(Basetest):

    @title("validate checkout page ")
    @pytest.fixture(scope='class')
    def test_checkout_page_title(self):
        global checkout_Page
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.username, TestData.password)
        cartPage = homePage.go_to_cart_page()
        checkout_Page=cartPage.click_checkout_button()
        final_header = checkout_Page.get_final_page_header()
        print(final_header)
        assert final_header == "Checkout: Your Information", f'invalid page header:{final_header}'

    @title(" validate checkout user data {firstname},{lastname},{postalcode}")
    def test_checkout_userdata(self,test_checkout_page_title):

        checkout_Page.get_your_information_page(TestData.firstname, TestData.lastname, TestData.postalcode)

        if TestData.firstname == "":
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_checkout_page_firstname.png")
            assert AssertionError == "Error : please enter username"
        elif TestData.lastname == "":
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_checkout_page_lastname.png")
            assert AssertionError == "Error : Please enter lastname"
        elif TestData.postalcode == "":
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_checkout_postalcode.png")
            assert AssertionError == "Error : Please enter PostalCode"
        elif TestData.firstname == TestData.lastname == TestData.postalcode == "":
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"firstname.png")
            assert AssertionError == "Error : enter firstname "
        elif TestData.lastname == TestData.postalcode == "":
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"lastname.png")
            assert AssertionError == "Error : enter lastname"
        else:
            checkout_Page.click_continue()
            assert True






