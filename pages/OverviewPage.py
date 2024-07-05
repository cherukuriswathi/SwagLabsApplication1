from pages.Utils import BasePage
from selenium.webdriver.common.by import By
from pages.WrapperPage import WrapperPage
from Config.swaglabs_logging import logger
class OverviewPage(BasePage):
    wrap_page_header=(By.CLASS_NAME,"title")
    click_finish = (By.ID, "finish")
    Summary_info=(By.CLASS_NAME,"title")

    def __init__(self, driver):
        super().__init__(driver)

    """validate overview page"""

    def get_page_header(self):
        logger.info("verifying the header of the page")
        return self.get_element_text(self.wrap_page_header)

    def get_summary_info(self):
        logger.info("verifying the text present inside the page")
        return self.get_element_text(self.Summary_info)

    """validate finish button"""

    def get_finish_text(self):
        logger.info("verify the text of finish button")
        finish_text = self.get_element_text(self.click_finish)
        return finish_text

    def click_finish_button(self):
        logger.info("verify the finish button is clickable or not")
        self.do_click(self.click_finish)
        return WrapperPage(self.driver)
