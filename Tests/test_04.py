import csv
import pytest
import time
import allure
from allure_commons.types import AttachmentType
import logging
import pandas as pd
import openpyxl

from Pages.CartPage import CartPage
from Pages.ContactPage import ContactPage
from Pages.HomePage import HomePage
from Pages.ShopPage import ShopPage

path = "./TestData/Jupiter_toys_test_data.xlsx"
write_data_path = "./TestData/Jupiter_toys_test_data.xlsx"


def readt_test_data():
    test_data = []
    data = pd.read_excel(path, sheet_name='tc_004', dtype=str)
    csvpath = './TestData/Jupiter_tous_test_data tc_004.csv'
    data.to_csv(csvpath, index= False) # convert xlsx data to csv for pytest parametrize fixture to read the data

    with open(csvpath, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data) # skip header row
        for row in data:
            test_data.append(row)
        return test_data


@allure.title("TC004")
@allure.description("Stuffed Frog, Funny cow & Valentine Bear toys purchase")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("testcasenum, product1, product1_count, product2, product2_count, product3, product3_count", readt_test_data()) # to excute the tests for multiple times
def test_shop_page_items(browser, testcasenum, product1, product1_count,	product2, product2_count, product3,	product3_count):

    home = HomePage(browser)
    home.homepage_title_check()

    shop = ShopPage(browser)
    # Buy stuffed frog, Fluffy bunny, Valentine bear
    shop.click_shop()
    shop.buy_frog_bunny_bear_toy(product1, product1_count, product2, product2_count, product3, product3_count)

    # verify item price, quantity & subtotal with total amount
    cart = CartPage(browser)
    cart.verify_item_price()
    cart.validate_price_total()


