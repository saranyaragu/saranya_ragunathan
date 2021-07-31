import csv
import pytest
import time
import allure
from allure_commons.types import AttachmentType
import logging
import pandas as pd
import openpyxl

from Pages.ContactPage import ContactPage
from Pages.HomePage import HomePage

path = "./TestData/Jupiter_toys_test_data.xlsx"
write_data_path = "./TestData/Jupiter_toys_test_data.xlsx"


def readt_test_data():
    test_data = []
    data = pd.read_excel(path, sheet_name='tc_001', dtype=str)
    csvpath = './TestData/Jupiter_toys_test_data.csv'
    data.to_csv(csvpath, index= False) # convert xlsx data to csv for pytest parametrize fixture to read the data

    with open(csvpath, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data) # skip header row
        for row in data:
            test_data.append(row)
        return test_data

@allure.title("TC001")
@allure.description("Validate Errors in the Contact Page")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("testcasenum, forename, surname, email, telephone, message", readt_test_data())
def test_contact_page_errors(browser, testcasenum, forename, surname, email, telephone, message):

    home = HomePage(browser)
    home.homepage_title_check()

    # Contact Page Mandatory field error check
    contact = ContactPage(browser)
    contact.contact_page_display_check()
    contact.contact_page_header_error_check()
    contact.contact_page_forename_error_check()
    contact.contact_page_email_error_check()
    contact.contact_page_message_error_check()

    # Contact Page Mandatory field error gone
    contact.contact_page_input(forename, email, message)
    contact.contact_page_validate_header_errors_gone()
    contact.contact_page_validate_forename_errors_gone()
    contact.contact_page_validate_email_errors_gone()
    contact.contact_page_validate_message_errors_gone()



