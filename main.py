from fastapi import FastAPI

from my_types import ResponseType
from time_table_scraper import time_table_scraper

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/mock')
def get_mock_data(starting_point: str, end_point: str) -> ResponseType:
    response: ResponseType = {
        'time_table': [
            {'time': ('07:18', '08:24'), 'type': 'local'},
            {'time': ('07:35', '08:33'), 'type': 'rapid'},
            {'time': ('08:06', '09:02'), 'type': 'local'}
        ]
    }
    return response


@app.get('/scraping')
def get_time_table(starting_point: str, end_point: str) -> ResponseType:
    response: ResponseType = time_table_scraper(starting_point, end_point)
    return response
