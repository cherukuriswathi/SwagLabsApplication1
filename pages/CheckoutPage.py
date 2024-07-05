from pages.Utils import BasePage
from selenium.webdriver.common.by import By
from pages.OverviewPage import OverviewPage
from Config.swaglabs_logging import logger

class CheckoutPage(BasePage):

    final_page_header = (By.CLASS_NAME, "title")
    firstname = (By.ID, "first-name")
    lastname = (By.ID, "last-name")
    Zipcode = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")

    def __init__(self, driver):
        super().__init__(driver)

    """validate checkout info page"""

    def get_final_page_header(self):
        logger.info("verifying the header of the checkout page")
        return self.get_element_text(self.final_page_header)

    def get_your_information_page(self, firstname, lastname, postalcode):
        logger.info("Enter firstname:")
        self.do_send_keys(self.firstname,  firstname)
        logger.info("Enter lastname:")
        self.do_send_keys(self.lastname, lastname)
        logger.info("Enter Zipcode")
        self.do_send_keys(self.Zipcode, postalcode)

    def click_continue(self):
        logger.info("click continue button")
        self.do_click(self.continue_button)
        return OverviewPage(self.driver)

