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
    data = pd.read_excel(path, sheet_name='tc_002', dtype=str)
    csvpath = 'C:/Users/Sara/PycharmProjects/PlanITJupiterToysAssignment/TestData/Jupiter_toys_test_data- tc_002.csv'
    # csvpath = './TestData/Jupiter_toys_test_data- tc_002.csv'
    data.to_csv(csvpath, index= False) # convert xlsx data to csv for pytest parametrize fixture to read the data

    with open(csvpath, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data) # skip header row
        for row in data:
            test_data.append(row)
        return test_data


@allure.title("TC002")
@allure.description("Successful contact submission in the Contact Page")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("testcasenum, forename, surname, email, telephone, message", readt_test_data()) # to excute the tests for multiple times
def test_contact_details_submission_check(browser, testcasenum, forename, surname, email, telephone, message):

    home = HomePage(browser)
    # home.homepage_title_check()

    # Add Mandatory details and contact submission
    contact = ContactPage(browser)
    contact.contact_page_display_check()
    contact.contact_page_input(forename, email, message)
    contact.contact_page_click_submit_bt()
    contact.submission_success_check()



