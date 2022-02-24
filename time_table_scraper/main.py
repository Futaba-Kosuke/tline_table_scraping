from typing import Final, Any, List, Tuple
from datetime import datetime
import requests

from bs4 import BeautifulSoup

from my_types import NavitimeParametersType, ResponseType

BASE_URL: Final[str] = 'https://www.navitime.co.jp/transfer/searchlist'


def get_time_table(rows: List[Any], railroad_areas: List[Any], url: str) -> ResponseType:
    return {
        'time_table': [
            {
                'time': get_train_time(rows[i]),
                'type': get_train_type(railroad_areas[i]),
                'transfer': get_train_transfer(rows[i])
            } for i in range(len(rows))
        ],
        'url': url
    }


def get_train_time(row: Any) -> Tuple[str, str]:
    time_str = row.find('dt', class_='left').text
    departure_time, arrival_time = time_str.split(u'\xa0⇒\xa0', 1)
    return (departure_time, arrival_time)


def get_train_type(railroad_area: Any) -> str:
    railroad_area_str = railroad_area.text
    if '区間快速' in railroad_area_str:
        return 'regional_rapid'
    elif '快速' in railroad_area_str:
        return 'rapid'
    else:
        return 'local'


def get_train_transfer(row: Any) -> int:
    transfer = row.find('dd', class_='required_transfer').find('div', class_='text').text.translate(
        str.maketrans({'\n': None, '\t': None, '乗': None, '換': None, '回': None}))
    if transfer.strip() == 'なし':
        return 0
    else:
        return int(transfer)


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
    # 最初に使用する鉄道を取得
    railroad_areas = [section.find('div', 'railroad-area') for section in
                      page.find_all('div', class_='section_detail_frame')]
    # 時刻の取得
    result: ResponseType = get_time_table(rows, railroad_areas, url)

    return result
