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
from Pages.ShopPage import ShopPage
from Pages.CartPage import CartPage

path = "./TestData/Jupiter_toys_test_data.xlsx"
write_data_path = "./TestData/Jupiter_toys_test_data.xlsx"


def readt_test_data():
    test_data = []
    data = pd.read_excel(path, sheet_name='tc_003', dtype=str)
    csvpath = './TestData/Jupiter_tous_test_data tc_003.csv'
    data.to_csv(csvpath, index=False)  # convert xlsx data to csv for pytest parametrize fixture to read the data

    with open(csvpath, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data) # skip header row
        for row in data:
            test_data.append(row)
        return test_data


@allure.title("TC003")
@allure.description("Funny cow & Fluffy Bunny toys purchase")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("testcasenum, product1, product1_count, product2, product2_count", readt_test_data()) # to excute the tests for multiple times
def test_shop_page_items(browser, testcasenum, product1, product1_count, product2, product2_count):

    home = HomePage(browser)
    home.homepage_title_check()

    # Buy Funny cow & Bunny toy
    shop = ShopPage(browser)
    shop.click_shop()
    shop.buy_funny_cow_toy(product1, product1_count)
    shop.buy_fluffy_bunny_toy(product2, product2_count)

    # Verify items in cart
    cart = CartPage(browser)
    cart.go_to_cart_page()
    cart.items_verify_in_cart()


