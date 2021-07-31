#######################################################################################################################
# Name          :  BasePage.py
# Created date  :  29-Jul-2021
# Created by    :  Sara
#
# Jupiter Toys Contact Page - Web Elements, Test Methods and Test verifications
########################################################################################################################
import logging
import re
import time

from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class BaseClass():

    """ Wrapper for selenium operations """

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_get_text(self, by_locator):
        text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        return text

    def do_assert_text(self, by_locator, asserttext):
        text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        assert text == asserttext

    def product_list_selection(self, by_locator1, by_locator2, arg1, arg2):
        lists = self.driver.find_elements_by_xpath(by_locator1)
        for i in range(len(lists)):
            ddmenu = lists[i]
            innerhtml = lists[i].get_attribute("innerHTML")
            if innerhtml == arg1:
                if lists[i].is_displayed():
                    for i in range(arg2):
                        self.driver.find_element_by_xpath(by_locator2).click()
                        time.sleep(5)
                else:
                    actions = ActionChains(self.driver)
                    time.sleep(2)
                    actions.move_to_element(lists[i]).click().perform()





