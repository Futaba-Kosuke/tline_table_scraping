from typing import Final
from urllib import request

from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()

TRANSFER_URL: Final[str] = 'https://www.navitime.co.jp/transfer/'


def access_page(starting_point: str, end_point: str) -> str:
    driver.get(TRANSFER_URL)

    driver.find_element_by_id('orv-station-name').send_keys(starting_point)
    driver.find_element_by_id('dnv-station-name').send_keys(end_point)

    driver.find_element_by_class_name('submit-container')

    return driver.current_url
