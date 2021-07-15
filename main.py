from fastapi import FastAPI

from my_types import ResponseType
from time_table_scraper import time_table_scraper

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/scraping')
def get_time_table(starting_point: str, end_point: str) -> ResponseType:
    response: ResponseType = time_table_scraper(starting_point, end_point)
    return response
