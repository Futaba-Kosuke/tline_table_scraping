from typing import List, Tuple, TypedDict
from pydantic import BaseModel

from fastapi import FastAPI


TrainType = TypedDict('TrainType', {
            'time': Tuple[str, str],
            'type': str 
        })

class RequestType (BaseModel):
    starting_point: str
    end_point: str

class ResponseType (TypedDict):
    time_table: List[TrainType]

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}
