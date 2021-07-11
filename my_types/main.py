from typing import List, Tuple, TypedDict

TrainType = TypedDict('TrainType', {
    'time': Tuple[str, str],
    'type': str
})

ResponseType = TypedDict('ResponseType', {
    'time_table': List[TrainType]
})