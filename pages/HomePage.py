from selenium.webdriver.common.by import By
from pages.Utils import BasePage
from pages.CartPage import CartPage
from Config.swaglabs_logging import logger

class HomePage(BasePage):
    element = (By.ID,"Swag Labs")

    header=(By.XPATH,"//*[@id='header_container']/div[2]/span")
    products_list=(By.XPATH,"//*[@id='inventory_container']/div/div/div[1]/div")
    add_cart_button=(By.ID, "add-to-cart-sauce-labs-backpack")
    cart_link_xpath = (By.XPATH,"//*[@id='shopping_cart_container']")
    cart_badge_text=(By.XPATH,"//*[@id='shopping_cart_container']/a/span")
    cart_page_header=(By.CSS_SELECTOR,"#header_container > div.header_secondary_container > span")

    def __init__(self, driver):
        super().__init__(driver)

    """ Validate homepage/products page products present in the page """
    def get_homepage_title(self, title):
        logger.info("verifying the title of the homepage")
        return self.get_title(title)

    def get_page_header(self):
        logger.info("verifying the header of the products page")
        return self.get_element_text(self.header)

    def get_product_titles(self):
        logger.info("verifying the name of each product ")
        product_titles = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [product_title.text for product_title in product_titles]

    def get_product_count(self):
        logger.info("verifying the total count of teh products present in the inventory items list")
        product_titles = self.get_product_titles()
        return len(product_titles)

    def go_to_cart_page(self):
        logger.info("verifying the add to cart button presence")
        self.do_click(self.add_cart_button)

        logger.info("verifying the add to cart link presence")
        self.do_click(self.cart_link_xpath)

        return CartPage(self.driver)



