from typing import List, Tuple, TypedDict

from fastapi import FastAPI

TrainType = TypedDict('TrainType', {
    'time': Tuple[str, str],
    'type': str
})


class ResponseType(TypedDict):
    time_table: List[TrainType]


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
