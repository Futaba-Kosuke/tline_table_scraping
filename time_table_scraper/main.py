from typing import Final
from urllib import request

from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary

from my_types import TrainType, ResponseType

TRANSFER_URL: Final[str] = 'https://www.navitime.co.jp/transfer/'


def access_page(starting_point: str, end_point: str) -> str:
    driver = webdriver.Chrome()

    driver.get(TRANSFER_URL)

    driver.find_element_by_id('orv-station-name').send_keys(starting_point)
    driver.find_element_by_id('dnv-station-name').send_keys(end_point)

    driver.find_element_by_class_name('submit-container').click()
    result: str = driver.current_url
    driver.close()

    return result


def format_time_str(time_str: str) -> TrainType:
    result: TrainType = {
        'time': tuple(time_str.split(u'\xa0⇒\xa0', 2)),
        'type': 'normal'
    }
    return result


def time_table_scraper(starting_point: str, end_point: str) -> ResponseType:
    url: str = access_page(starting_point, end_point)

    response = request.urlopen(url)
    page = BeautifulSoup(response)
    response.close()

    # 時刻表の取得
    rows = page.find_all('dl', class_='summay_route')
    # 時刻の取得
    time_table = [format_time_str(row.find('dt', class_='left').text) for row in rows]

    result: ResponseType = {
        'time_table': time_table
    }

    return result
