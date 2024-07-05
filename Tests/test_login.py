import os.path
import time

import pytest
from allure_commons._allure import title
from Config.config import TestData
from pages.LoginPage import LoginPage
from Tests.test_base import Basetest
import allure
from Config.swaglabs_logging import logger

class TestLogin(Basetest):

    @title("validate login page")
    @pytest.fixture(scope='class')
    def test_login_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.login_page_title)
        assert title == TestData.login_page_title


    @title("Perform login with username {username} and password {password}")

    def test_login(self,test_login_title):

        if TestData.username == "":
            allure.attach(self.driver.get_screenshot_as_png(), name='login_NoUsername', attachment_type=allure.attachment_type.PNG)
            #self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"login_page1.png")
            assert AssertionError == "Username required"
        elif TestData.username != "standard_user":
            allure.attach(self.driver.get_screenshot_as_png(), name='login_IncorrectUsername', attachment_type=allure.attachment_type.PNG)
            #self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"login_page1.png")

            assert AssertionError == "Epic sadface: Username and password do not match any user in this service"
        elif TestData.password == "":

            allure.attach(self.driver.get_screenshot_as_png(), name='login_NoPassword', attachment_type=allure.attachment_type.PNG)

            assert AssertionError == "password required"
        elif TestData.password != "secret_sauce":
            allure.attach(self.driver.get_screenshot_as_png(), name='login_IncorrectPassword', attachment_type=allure.attachment_type.PNG)
            assert AssertionError == "Epic sadface: Username and password do not match any user in this service"
        else:
            assert True


