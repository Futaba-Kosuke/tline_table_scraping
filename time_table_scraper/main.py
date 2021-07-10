from typing import Final
from urllib import request

from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()

TRANSFER_URL: Final[str] = 'https://www.navitime.co.jp/transfer/'


def access_page(starting_point: str, end_point: str) -> str:
    driver = webdriver.Chrome()
    driver.get(TRANSFER_URL)
    return 'WIP'
