import datetime
import json
import logging
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
config_path = './Tests/config.json'
supported_browsers = ['Chrome', 'Firefox']
Default_waittime = 10


@pytest.fixture(scope='session')
def config():
    # open config file and read json data to return it as dict
    with open(config_path) as config_file:
        if os.path.isfile(config_path):
            data = json.load(config_file)
            return data
        else:
            raise Exception("file does not exists")


@pytest.fixture()
def browser_config(config):
    if 'browser' not in config:
        raise Exception("No browser details in the file")
    elif config['browser'] not in supported_browsers:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture()
def headless_config(config):
    return config['headless']


@pytest.fixture()
def waittime_config(config):
    return config['wait_time'] if 'wait_time' in config else Default_waittime


@pytest.fixture()
def url_config(config):
    return config['url']


@pytest.fixture()
def browser(browser_config, headless_config, waittime_config, url_config):
    if browser_config == 'Chrome':
        if headless_config == "Y":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            driver = webdriver.Chrome(options=chrome_options)
            driver.delete_all_cookies()
        else:
            chrome_options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(options=chrome_options)
            driver.delete_all_cookies()
    elif browser_config == 'Firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser is not a supported browser")
    logging.info("Run started at:" + str(datetime.datetime.now()))
    driver.implicitly_wait(waittime_config)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(url_config)

    yield driver

    driver.close()
    driver.quit()






