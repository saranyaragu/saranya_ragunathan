#######################################################################################################################
# Name          :  ContactPage.py
# Created date  :  29-Jul-2021
# Created by    :  Sara
#
# Jupiter Toys Contact Page - Web Elements, Test Methods and Test verifications
########################################################################################################################

import logging
import time
from selenium import webdriver

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from Pages.BasePage import BaseClass

LOGGER = logging.getLogger(__name__)


class ContactPage(BaseClass):

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

    # Method for Contactpage - Forename field
    @staticmethod
    def element_forename_input(self):
        forename_input_id = (By.ID, 'forename')
        return forename_input_id

    # Method for Contactpage - Surname field
    @staticmethod
    def element_surname_input(self):
        Surname_input_id = 'surname'
        return Surname_input_id

    # Method for Contactpage - Email field
    @staticmethod
    def element_email_input(self):
        email_input_csv = (By.CSS_SELECTOR,'#email')
        return email_input_csv

    # Method for Contactpage - Telephone field
    @staticmethod
    def element_telephone_input(self):
        telephone_input_id = (By.ID, 'telephone')
        return telephone_input_id

    # Method for Contactpage - Message field
    @staticmethod
    def element_message_input(self):
        message_input_id = (By.ID, 'message')
        return message_input_id

    # Method for Contactpage - Submit button
    @staticmethod
    def element_submit_button(self):
        submit_button_xpath = '//div[@class="form-actions"]/a'
        return submit_button_xpath

    # Method for Contactpage - Header field error
    @staticmethod
    def element_header_error_text(self):
        self.header_error_text_xpath = "//div[@class='alert alert-error ng-scope']"
        return self.header_error_text_xpath

    # Method for Contactpage - Forename field error
    @staticmethod
    def element_forename_error_text(self):
        self.forename_error_text_id = 'forename-err'
        return self.forename_error_text_id

    # Method for Contactpage - Email field error
    @staticmethod
    def element_email_error_text(self):
        self.email_error_text_css = '#email-err'
        return self.email_error_text_css

    # Method for Contactpage - Message field error
    @staticmethod
    def element_message_error_text(self):
        message_error_text_id = 'message-err'
        return message_error_text_id

    # Method for Contactpage - header title field
    @staticmethod
    def element_header_text(self):
        header_text_xpath = '//*[@id="header-message"]/div/strong'
        return header_text_xpath

    # Method for Contactpage - submission success message
    @staticmethod
    def element_submission_success_message(self):
        message = "//div[@class='alert alert-success']"
        return message

    ########################################################################################################################
    # Page Methods
    ########################################################################################################################

    # Test Case-001 methods
    # Method for validating the contact page mandatory field errors
    def contact_page_display_check(self):
        self.driver.find_element_by_xpath('//*[@id="nav-contact"]/a').click()
        if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, ContactPage.element_header_text(self)))).is_displayed:
            header_text = self.driver.find_element_by_xpath(ContactPage.element_header_text(self)).text
            logging.info("Header text displayed in contact page is %s", header_text)
            actual_text = "We welcome your feedback"
            assert header_text, actual_text
            logging.info("Contact Page is displayed")

    # Method for validating the contact page forename missing data error
    def contact_page_header_error_check(self):
        self.driver.find_element_by_xpath(ContactPage.element_submit_button(self)).click()
        logging.info("Submit button is clicked without key in any data")
        # Error message check in Header section
        if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, ContactPage.element_header_error_text(self)))).is_displayed:
            header_error_text = self.driver.find_element_by_xpath(ContactPage.element_header_error_text(self)).text
            expected_error_text = "but we won't get it unless you complete the form correctly."
            assert header_error_text, expected_error_text
            logging.info("Correct header error message '%s' is displayed", header_error_text)

    # Method for validating the contact page forename missing data error
    def contact_page_forename_error_check(self):
        # fore name Error message check
        if(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,ContactPage.element_forename_error_text(self))))).is_displayed:
            forename_error_text = self.driver.find_element_by_id(ContactPage.element_forename_error_text(self)).text
            if forename_error_text == "Forename is required":
                logging.info("Forename missing error message: '%s' is displayed", forename_error_text)

    # Method for validating the contact page Email missing data error
    def contact_page_email_error_check(self):
        # Email Error message check
        if(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ContactPage.element_email_error_text(self))))).is_displayed:
            email_error_text = self.driver.find_element_by_css_selector(ContactPage.element_email_error_text(self)).text
            logging.info(email_error_text)
            if email_error_text == "Email is required":
                logging.info("Email missing error message: '%s' is displayed", email_error_text)

    # Method for validating the contact page Email missing data error
    def contact_page_message_error_check(self):
        # Message Error check
        if(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,ContactPage.element_message_error_text(self))))).is_displayed:
            message_error_text = self.driver.find_element_by_id(ContactPage.element_message_error_text(self)).text
            if message_error_text == "Message is required":
                logging.info("Message missing error message: '%s' is displayed", message_error_text)
        allure.attach(self.driver.get_screenshot_as_png(), name='contact page errors', attachment_type=AttachmentType.PNG)

    # TC_002 methods
    # Method to populate mandatory fields in contact page
    def contact_page_input(self, forename, email, message):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        # forename input
        self.do_click(ContactPage.element_forename_input(self))
        self.do_send_keys(ContactPage.element_forename_input(self), forename)
        logging.info("Forename '%s' is entered", forename)
        # email input
        self.do_click(ContactPage.element_email_input(self))
        self.do_send_keys(ContactPage.element_email_input(self), email)
        logging.info("Email '%s' is entered", email)
        # message input
        self.do_click(ContactPage.element_message_input(self))
        self.do_send_keys(ContactPage.element_message_input(self), message)
        logging.info("Message '%s' is entered", message)
        allure.attach(self.driver.get_screenshot_as_png(), name='contact page data entry', attachment_type=AttachmentType.PNG)

    # Method to validate mandatory fields errors are gone in contact page

    # Method to validate header error is gone
    def contact_page_validate_header_errors_gone(self):
        try:
            if self.driver.find_element_by_xpath(ContactPage.element_header_text(self)).is_displayed:
                logging.info("Header error message is gone after key in mandatory fields ")
        except NoSuchElementException as e:
            logging.info(" No header error message is displayed")

    # Method to validate forename error is gone
    def contact_page_validate_forename_errors_gone(self):
        try:
            if self.driver.find_element_by_xpath(ContactPage.element_forename_error_text(self)).is_displayed:
                logging.info("forename error message is still displayed")
        except NoSuchElementException as e:
            logging.info(" Forename error message is gone")

    # Method to validate email error is gone
    def contact_page_validate_email_errors_gone(self):
        try:
            if self.driver.find_element_by_xpath(ContactPage.element_email_error_text(self)).is_displayed:
                logging.info("email error message is still displayed")
        except NoSuchElementException as e:
            logging.info(" Email error message is gone")

    # Method to validate message error is gone
    def contact_page_validate_message_errors_gone(self):
        try:
            if self.driver.find_element_by_xpath(ContactPage.element_message_error_text(self)).is_displayed:
                logging.info("error message is still displayed")
        except NoSuchElementException as e:
            logging.info(" Message field error is gone")

    # Method to click submit button
    def contact_page_click_submit_bt(self):
        self.driver.find_element_by_xpath(ContactPage.element_submit_button(self)).click()

    # Method to validate success submission message
    def submission_success_check(self):
        if (WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.XPATH,ContactPage.element_submission_success_message(self))))).is_displayed:
            actual_submission_message = self.driver.find_element_by_xpath(ContactPage.element_submission_success_message(self))
            expected_submission_message = 'Thanks test, we appreciate your feedback.'
            assert expected_submission_message, actual_submission_message
            logging.info("Successful submission message is displayed")
            allure.attach(self.driver.get_screenshot_as_png(), name='Submission success message', attachment_type=AttachmentType.PNG)













