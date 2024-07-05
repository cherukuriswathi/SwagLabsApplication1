from pages.Utils import BasePage
from selenium.webdriver.common.by import By
from Config.swaglabs_logging import logger
from pages.CheckoutPage import CheckoutPage


class CartPage(BasePage):
    cart_link_xpath = (By.XPATH, "//*[@id='shopping_cart_container']/a")
    cart_page_title =(By.CLASS_NAME,"title")
    cart_container=(By.XPATH,"//*[@id='cart_contents_container']/div/div[1]/div[3]")
    remove_button=(By.XPATH,"//*[@class='btn btn_secondary btn_small btn_inventory ']")
    item_price=(By.CLASS_NAME,"inventory_item_price")
    Checkout_button = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    """Validate cart page and products in the cart"""

    def click_cart_link(self):
        logger.info("verifying the cart link is clickable or not")
        return self.do_click(self.cart_link_xpath)

    def get_cart_product_titles(self):
        logger.info("verifying the products present in the cart ")
        product_titles = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [product_title.text for product_title in product_titles]

    def get_cart_product_count(self):
        logger.info("verifying the count of products present in the cart")
        product_titles = self.get_cart_product_titles()
        return len(product_titles)

    """Validate checkout button"""

    def get_checkout_text(self):
        logger.info("verifying the text of checkout button")
        return self.get_element_text(self.Checkout_button)

    def click_checkout_button(self):
        logger.info("verifying the checkout button is clickable or not")
        self.do_click(self.Checkout_button)
        return CheckoutPage(self.driver)





