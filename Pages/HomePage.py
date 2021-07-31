#######################################################################################################################
# Name          :  HomePage.py
# Created date  :  29-Jul-2021
# Created by    :  Sara
#
# Jupiter Toys Home Page - Web Elements, Test Methods and Test verifications
########################################################################################################################

import logging
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from Pages.BasePage import BaseClass
LOGGER = logging.getLogger(__name__)


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

########################################################################################################################
# Page Elements
########################################################################################################################

    # Method for Homepage - Contact Link field
    @staticmethod
    def element_contact_link(self):
        contact_link_xpath = '//*[@id="nav-contact"]'
        return contact_link_xpath

########################################################################################################################
# Page Methods
########################################################################################################################
    # Method for Jupiter Toys Homepage title check
    def homepage_title_check(self):
        expected_home_page_title = 'Jupiter Toys'
        actual_home_page_title = self.driver.title
        logging.info("Page title is %s", actual_home_page_title)
        assert(expected_home_page_title, actual_home_page_title)
        logging.info(" correct jupiter toys is displayed")

    # Method for contact link click
    def homepage_contact_link_click(self):
        self.do_click(HomePage.element_contact_link(self))
        logging.info("Contact link option is displayed and clicked from Home Page")

    # Method for shop link click
    def homepage_shop_link_click(self):
        self.do_click(HomePage.element_contact_link(self))
        logging.info("Contact link option is displayed and clicked from Home Page")























