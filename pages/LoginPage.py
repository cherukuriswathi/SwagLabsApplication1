from selenium.webdriver.common.by import By
from pages.Utils import BasePage
from Config.config import TestData
from pages.HomePage import HomePage
from Config.swaglabs_logging import logger


class LoginPage(BasePage):
    # logger = logging.getLogger(__name__)

    textbox_username = (By.ID, "user-name")
    textbox_password_id = (By.ID, "password")
    button_login_xpath = (By.XPATH, "//*[@id='login-button']")
    error_message = "//*[@id='login_button_container']/div/form/div[3]/h3"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.URL)
        self.driver = driver

    """ validate the login Page title"""

    def get_login_title(self, title):
        return self.get_title(title)

    """validate username and password fields"""

    def do_login(self, username, password):
        logger.info("Enter username : " + username)
        self.do_send_keys(self.textbox_username, username)
        logger.info("Enter password : " + password)
        self.do_send_keys(self.textbox_password_id, password)
        logger.info("Click login button")
        self.do_click(self.button_login_xpath)
        return HomePage(self.driver)





