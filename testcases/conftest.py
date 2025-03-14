import pytest
from selenium import webdriver
from configparser import ConfigParser


@pytest.fixture(scope='session', autouse=True)
def driver():
    config = ConfigParser()
    config.read('../pytest.ini')
    URL = config.get('browser', 'URL')
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(URL)
    yield browser
    browser.quit()
    