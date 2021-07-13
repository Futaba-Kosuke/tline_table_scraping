from typing import Final
from datetime import datetime
import requests

from bs4 import BeautifulSoup

from my_types import NavitimeParametersType, TrainType, ResponseType

BASE_URL: Final[str] = 'https://www.navitime.co.jp/transfer/searchlist'


def format_time_str(time_str: str) -> TrainType:
    departure_time, arrival_time = time_str.split(u'\xa0⇒\xa0', 2)
    result: TrainType = {
        'time': (departure_time, arrival_time),
        'type': 'normal'
    }
    return result


def time_table_scraper(starting_point: str, end_point: str) -> ResponseType:
    now = datetime.now()
    payloads: NavitimeParametersType = {
        'orvStationName': starting_point,
        'orvStationCode': '',
        'dnvStationName': end_point,
        'dnvStationCode': '',
        'thr1StationName': '',
        'thr1StationCode': '',
        'thr2StationName': '',
        'thr2StationCode': '',
        'thr3StationName': '',
        'thr3StationCode': '',
        'year': str(now.year),
        'month': str(now.month),
        'day': str(now.day),
        'hour': str(now.hour),
        'minute': str(now.minute),
        'basis': '1',
        'freePass': '0',
        'sort': '4',
        'wspeed': '100',
    }
    response = requests.get(BASE_URL, params=payloads)
    url: str = response.url

    page = BeautifulSoup(response.content, 'html.parser')

    # 時刻表の取得
    rows = page.find_all('dl', class_='summay_route')
    # 時刻の取得
    time_table = [format_time_str(row.find('dt', class_='left').text) for row in rows]

    result: ResponseType = {
        'time_table': time_table
    }

    return result
