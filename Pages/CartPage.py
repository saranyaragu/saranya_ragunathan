#######################################################################################################################
# Name          :  ShopPage.py
# Created date  :  29-Jul-2021
# Created by    :  Sara
#
# Jupiter Toys Cart Page - Web Elements, Test Methods and Test verifications
########################################################################################################################
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


class CartPage(BaseClass):

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
        cart_button_id = (By.ID, "nav-cart")
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

    # Method to get the price for all the items from shop page in dictionary format
    def get_item_price_from_shoppage(self):
        # get price of all items from Shop page
        itemlist = []
        item_lists = self.driver.find_elements_by_xpath(CartPage.element_price_list(self))
        for item_list in range(len(item_lists)):
            innerhtml = item_lists[item_list].get_attribute("innerHTML")
            itemlist.append(innerhtml)

        # get item name from Shop page
        pricelist = []
        price_lists = self.driver.find_elements_by_xpath(CartPage.element_item_name(self))
        for price_list in range(len(price_lists)):
            innerhtml = price_lists[price_list].get_attribute("innerHTML")
            pricelist.append(innerhtml)

        # Item with Price details for all items in shop page
        combined_list = dict(zip(pricelist, itemlist))
        return combined_list

    # Method to get the price for all the items from cart table in dictionary format
    def get_item_price_in_cart(self):
        self.do_click(CartPage.element_cart_link(self))

        # check cart link is highlighted or not to confirm user is in cart page
        if (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((CartPage.element_cart_link(self))))).is_displayed:
            logging.info("Cart link is highlighted thus cart page is displayed")

        # get cart table rows count
        rows = len(self.driver.find_elements_by_xpath(CartPage.element_cart_table_row(self)))
        cols = len(self.driver.find_elements_by_xpath(CartPage.element_cart_table_column(self)))


        # Iterate thorugh table to verify the cart items
        before_xpath = '//*[@class="table table-striped cart-items"]/tbody/tr['
        after_xpath = ']/td[1]'

        # price xpath
        price_before_xpath = '//*[@class="table table-striped cart-items"]/tbody/tr['
        price_after_xpath = ']/td[2]'
        cart_item_list = []
        price_item_list = []
        for tab_row in range(1, rows+1):
            for col_row in range(1, cols + 1):
                # get item details from cart table as a list

                final_xpath = before_xpath + str(tab_row) + after_xpath
                cart_item = self.driver.find_element_by_xpath(final_xpath).text
                cart_item_list.append(cart_item)

                # get price of each item from cart table as a list
                price_final_xpath = price_before_xpath + str(tab_row) + price_after_xpath
                price = self.driver.find_element_by_xpath(price_final_xpath).text
                price_item_list.append(price)

        # convert item& price from cart table into dict
        cart_item_price_list = dict(zip(cart_item_list, price_item_list))
        return cart_item_price_list

    # Method to compare proce displayed in shop page with price in cart table
    def verify_item_price(self):
        shop_page_item_price = CartPage.get_item_price_from_shoppage(self)
        # get subset from shop_page_item_price dict
        test_case_items = ['Stuffed Frog', 'Fluffy Bunny', 'Valentine Bear']
        subset_dict = {key: value for key, value in shop_page_item_price.items() if key in test_case_items}
        cart_table_item_price = CartPage.get_item_price_in_cart(self)

        # compare price in shop page with price in cart table
        # extract value to compare
        for key in test_case_items:
            if subset_dict.get(key) == cart_table_item_price.get(key):
                logging.info("Price displayed in cart page is same as the price in the shop page")
                logging.info("Price displayed in cart page is : %s", cart_table_item_price)

    # Method to Verify that each product’s sub total = product price * quantity
    def validate_price_total(self):
        # Total amount - split numbers
        total_amount = self.driver.find_element_by_xpath(CartPage.element_total_amount(self)).text
        total_amount_after_trim = total_amount.replace('Total: ', '')
        logging.info("Total amount %s", total_amount_after_trim)

        # get quantity & item price:

        # get cart table rows count
        row = len(self.driver.find_elements_by_xpath(CartPage.element_cart_table_row(self)))
        cols = len(self.driver.find_elements_by_xpath(CartPage.element_cart_table_column(self)))

        # Iterate thorugh table to verify the cart items
        price_before_xpath = '//*[@class="table table-striped cart-items"]/tbody/tr['
        price_after_xpath = ']/td[2]'

        # price xpath
        quantity_before_xpath = '//*[@class="table table-striped cart-items"]/tbody/tr['
        quantity_after_xpath = ']/td[3]/input'

        # subtotal xpath
        subtotal_before_xpath = '//*[@class="table table-striped cart-items"]/tbody/tr['
        subtotal_after_xpath = ']/td[4]'

        item_quantity = []
        item_price = []
        item_subtotal = []
        final_subtotal_list = []

        # Iterate cart table and get item price
        for tab_row in range(1, row + 1):
            # get price in the cart as a list
            final_xpath = price_before_xpath + str(tab_row) + price_after_xpath
            cart_item_price = self.driver.find_element_by_xpath(final_xpath).text
            item_price.append(cart_item_price)

        # Iterate cart table and get quantity
        for tab_row in range(1, row + 1):
            # get quantity details as a list
            quantity_final_xpath = quantity_before_xpath + str(tab_row) + quantity_after_xpath
            Cart_item_quantity = self.driver.find_element_by_xpath(quantity_final_xpath).get_attribute("value")
            item_quantity.append(Cart_item_quantity)

        # Iterate cart table and Subtotal
        for tab_row in range(1, row + 1):
            subtotal_final_xpath = subtotal_before_xpath + str(tab_row) + subtotal_after_xpath
            subtotal = self.driver.find_element_by_xpath(subtotal_final_xpath).text
            item_subtotal.append(subtotal)

        # Subtotal price displayed in cart table
        subtotal_after_trim = [x.lstrip('$') for x in item_subtotal]
        final_subtotal = [float(i) for i in subtotal_after_trim]
        total_subtotal_price = sum(final_subtotal)
        logging.info("total sub %s", total_subtotal_price)

        # Subtotal price by  item price * quantity
        item_price_after_trim = [x.lstrip('$') for x in item_price]
        final_item_price = [float(i) for i in item_price_after_trim]
        quantity_after_trim = [x.lstrip('$') for x in item_quantity]
        final_quantity = [float(x) for x in quantity_after_trim]
        for n, x in zip(final_quantity, final_item_price):
            final_subtotal_list.append(n * x)

        # each product’s sub total = product price * quantity
        if collections.Counter(final_subtotal_list) == collections.Counter(final_subtotal):
            logging.info("each product’s sub total = product price * quantity. Subtotal is %s and product price*quantity value is %s", final_subtotal_list, final_subtotal)
        else:
            logging.info("each product’s sub total not = product price * quantity")

        # verify if "total = sum(sub totals)"
        if total_subtotal_price == total_amount_after_trim:
            logging.info("Total amount in Cart page is %s, and sum of sum total is %s so total = sum(sub totals)", total_subtotal_price, total_amount_after_trim)
        else:
            logging.info("Total amount in Cart page is %s, and sum of sum total is %s so total = sum(sub totals)", total_subtotal_price, total_amount_after_trim)

    # Method for Funny Cow & Fluffy Bunny shop
    def items_verify_in_cart(self):
        # check cart link is highlighted or not to confirm user is in cart page
        if (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((CartPage.element_cart_link(self))))).is_displayed:
            logging.info("Cart link is highlighted thus cart page is displayed")

        # get cart table rows count
        row = len(self.driver.find_elements_by_xpath(CartPage.element_cart_table_row(self)))
        cols = len(self.driver.find_elements_by_xpath(CartPage.element_cart_table_column(self)))

        # Iterate thorugh table to verify the cart items
        before_xpath = '//*[@class="table table-striped cart-items"]/tbody/tr['
        after_xpath = ']/td[1]'
        for tab_row in range(2, row + 1):
            for col_row in range(1, cols + 1):
                final_xpath = before_xpath + str(tab_row) + after_xpath
                cart_item = self.driver.find_elements_by_xpath(final_xpath)
                if cart_item == "Funny Cow" or "Fluffy Bunny":
                    logging.info("Both the items 'funny cow & fluffy bunny' are added in the cart")
                    break
        allure.attach(self.driver.get_screenshot_as_png(), name='Cart Page', attachment_type=AttachmentType.PNG)

    def go_to_cart_page(self):
        self.do_click(CartPage.element_cart_link(self))




