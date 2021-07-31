#######################################################################################################################
# Name          :  ShopPage.py
# Created date  :  29-Jul-2021
# Created by    :  Sara
#
# Jupiter Toys Home Page - Web Elements, Test Methods and Test verifications
########################################################################################################################
import ast
import json
import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from Pages.BasePage import BaseClass
import collections

LOGGER = logging.getLogger(__name__)


class ShopPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    ########################################################################################################################
    # Page Elements
    ########################################################################################################################

    # Method for Shop page - funny cow field

    @staticmethod
    def element_common_buy_button(self):
        button_xpath = '//*[@class="product ng-scope"]/div/p/a'
        return button_xpath

    # Element property to get all the products as a list
    @staticmethod
    def element_all_products_link(self):
        list = '//div[@class="products ng-scope"]/ul//li//div//h4'
        return list

    @staticmethod
    def element_funnycow_buy_button(self):
        button_xpath = '//*[@id="product-6"]/div/p/a'
        return button_xpath

    # Method for Shop page - fluppy bunny field
    @staticmethod
    def element_fluffy_bunny_buy_button(self):
        button_css = '//*[@id="product-4"]/div/p/a'
        return button_css

    # Method for Shop page - Stuffed Frog field
    @staticmethod
    def element_stuffed_frog_buy_button(self):
        button_xpath = "//div[@class='products ng-scope']/ul/li[@id='product-2']/div/p/a"
        return button_xpath

    # Method for Shop page -valentine bear field
    @staticmethod
    def element_valentine_bear_buy_button(self):
        button_xpath = "//div[@class='products ng-scope']/ul/li[@id='product-7']/div/p/a"
        return button_xpath

    # Method for Shop page -handmade doll field
    @staticmethod
    def element_handmade_doll_buy_button(self):
        button_xpath = "//div[@class='products ng-scope']/ul/li[@id='product-3']/div/p/a"
        return button_xpath

    # Method for Shop page - smiley bear field
    @staticmethod
    def element_smiley_bear_buy_button(self):
        button_xpath = "//div[@class='products ng-scope']/ul/li[@id='product-5']/div/p/a"
        return button_xpath

    # Method for Shop page - Stuffed Frog field
    @staticmethod
    def element_smiley_face_buy_button(self):
        button_xpath = "//div[@class='products ng-scope']/ul/li[@id='product-8']/div/p/a"
        return button_xpath

    # Method for Shop page - teddy bear field
    @staticmethod
    def element_teddy_bear_buy_button(self):
        button_xpath = "//div[@class='products ng-scope']/ul/li[@id='product-1']/div/p/a"
        return button_xpath

    # Method for Shop page - cart number
    @staticmethod
    def element_cart_number_input(self):
        cart_button_xpath = '//*[@id="nav-cart"]/a/span'
        return cart_button_xpath

    # Method for Shop page - cart number
    @staticmethod
    def element_cart_link(self):
        cart_button_id = (By.XPATH, '//*[@id="nav-cart"]/a')
        return cart_button_id

    # Method for Shop page - cart link highlight
    @staticmethod
    def element_cart_link_highlight_check(self):
        highlight_text_xpath = "//div[@class='nav-collapse']/ul[@class='nav pull-right ng-scope']/li[@id='nav-cart'and@class='active']"
        return highlight_text_xpath

    # Method for Shop page - cart table row
    @staticmethod
    def element_cart_table_row(self):
        row = '//*[@class="table table-striped cart-items"]/tbody/tr'
        return row

    # Method for Shop page - cart table row
    @staticmethod
    def element_cart_table_column(self):
        cols = '//*[@class="table table-striped cart-items"]/tbody/tr[2]/td'
        return cols

    # Method for Shop page - price details for all the items
    @staticmethod
    def element_price_list(self):
        price = '//*[@class="product ng-scope"]/div/p/span'
        return price

    # Method for Shop page - item name for all the items
    @staticmethod
    def element_item_name(self):
        price = '//*[@class="product ng-scope"]/div/h4'
        return price

    # Method for cart page - total
    @staticmethod
    def element_total_amount(self):
        price = '/html/body/div[2]/div/form/table/tfoot/tr[1]/td/strong'
        return price

    # Method for shop link from Home Page
    @staticmethod
    def element_shop_bt_link(self):
        bt = (By.CSS_SELECTOR, '#nav-shop > a')
        return bt

    ######################"##################################################################################################
    # Page Methods
    ########################################################################################################################
    # TC_003

    # Method to click shop button from Home Page
    def click_shop(self):
        self.do_click(ShopPage.element_shop_bt_link(self))
        logging.info("Shop button is clicked from Home Page")

    # Method to buy funny cow toys
    def buy_funny_cow_toy(self, product1, product1_count):
        cow_toys_count = int(float(product1_count))

        # check the cart number before adding cow toys
        cart_value = int(self.driver.find_element_by_xpath(ShopPage.element_cart_number_input(self)).text)
        if cart_value < 1:
            logging.info("Cart is empty before adding toys")

        # double click funny cow buy button using commom test method product selection
        self.product_list_selection(ShopPage.element_all_products_link(self), ShopPage.element_funnycow_buy_button(self), product1, int(float(product1_count)))

        # check funny cow is added to cart
        actual_cart_value_after_adding_cow = int(self.driver.find_element_by_xpath(ShopPage.element_cart_number_input(self)).text)
        expected_cart_value_after_adding_cow = cart_value + cow_toys_count

        if actual_cart_value_after_adding_cow == expected_cart_value_after_adding_cow:
            logging.info(" %s funny cow is added in the cart", actual_cart_value_after_adding_cow)
        else:
            logging.info("2 funny cow is not added, actual is %s", actual_cart_value_after_adding_cow)
        allure.attach(self.driver.get_screenshot_as_png(), name='Shop_page_after_adding_funny_cow', attachment_type=AttachmentType.PNG)

    # Method to buy fluffy bunny toys
    def buy_fluffy_bunny_toy(self, product2, product2_count):
        # check cart number before adding bunny toys
        cart_value_before_adding_bunny = int(self.driver.find_element_by_xpath(ShopPage.element_cart_number_input(self)).text)
        logging.info("Cart number before selecting the bunny toys is: %s", cart_value_before_adding_bunny)

        # fluffy bunny buy option
        self.product_list_selection(ShopPage.element_all_products_link(self), ShopPage.element_fluffy_bunny_buy_button(self), product2, int(float(product2_count)))
        logging.info("Fluffy bunny buy option is selected")

        # check fluffy bunny is added to cart
        actual_cart_value_after_adding_bunny = int(self.driver.find_element_by_xpath(ShopPage.element_cart_number_input(self)).text)
        expected_cart_value_after_adding_bunny = int(cart_value_before_adding_bunny + int(float(product2_count)))
        if actual_cart_value_after_adding_bunny == expected_cart_value_after_adding_bunny:
            logging.info(" %s fluffy bunny is added in the cart", int(float(product2_count)))
        else:
            logging.info("1 funny cow is not added, actual is %s", actual_cart_value_after_adding_bunny)
        allure.attach(self.driver.get_screenshot_as_png(), name='Shop_page_after_adding_fluffy_bunny', attachment_type=AttachmentType.PNG)

    # Method to add Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear
    def buy_frog_bunny_bear_toy(self, product1, product1_count,product2, product2_count, product3, product3_count):
        # check the cart number before adding cow toys
        cart_value = int(self.driver.find_element_by_xpath(ShopPage.element_cart_number_input(self)).text)
        if cart_value < 1:
            logging.info("Cart is empty before adding toys")

        # buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear using common method
        self.product_list_selection(ShopPage.element_all_products_link(self), ShopPage.element_stuffed_frog_buy_button(self), product1, int(float(product1_count)))
        self.product_list_selection(ShopPage.element_all_products_link(self), ShopPage.element_fluffy_bunny_buy_button(self), product2, int(float(product2_count)))
        self.product_list_selection(ShopPage.element_all_products_link(self), ShopPage.element_valentine_bear_buy_button(self), product3, int(float(product3_count)))

        frog_toy_count = int(float(product1_count))
        bunny_toy_count = int(float(product2_count))
        bear_toy_count = int(float(product3_count))

        actual_cart_value_after_adding_toys = int(self.driver.find_element_by_xpath(ShopPage.element_cart_number_input(self)).text)
        expected_cart_value_after_adding_toys = frog_toy_count + bunny_toy_count + bear_toy_count
        if actual_cart_value_after_adding_toys == expected_cart_value_after_adding_toys:
            logging.info(" %s Stuffed frog, %s Fluffy bunny, %s Valentine Bear is added in the cart", frog_toy_count, bunny_toy_count, bear_toy_count)
        else:
            logging.info("Toys are not added, actual is %s", actual_cart_value_after_adding_toys)
        allure.attach(self.driver.get_screenshot_as_png(), name='Shop_page_after_adding_fluffy_bunny', attachment_type=AttachmentType.PNG)








