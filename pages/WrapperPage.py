from pages.Utils import BasePage

from selenium.webdriver.common.by import By
from Config.swaglabs_logging import logger

class WrapperPage(BasePage):
    page_header=(By.CLASS_NAME,"title")
    wrapper_text = (By.XPATH, "//*[@id='checkout_complete_container']/h2")
    back_home_button = (By.CSS_SELECTOR, "#back-to-products")


    def __init__(self,driver):
        super().__init__(driver)

    """ validate wrapping page """

    def get_page_header(self):
        logger.info("verify the page header")
        return self.get_element_text(self.page_header)

    def get_wrapper_text(self):
        logger.info("verify the text present inside the page")
        return self.get_element_text(self.wrapper_text)

    """ validate back home button"""

    def get_back_home_text(self):
        logger.info("verify back home button text")
        return self.get_element_text(self.back_home_button)

    def click_back_home(self):
        logger.info("verify back home button")
        self.do_click(self.back_home_button)





