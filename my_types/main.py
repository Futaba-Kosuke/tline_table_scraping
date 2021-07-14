from typing import List, Tuple, TypedDict

TrainType = TypedDict('TrainType', {
    'time': Tuple[str, str],
    'type': str,
    'transfer': int
})

ResponseType = TypedDict('ResponseType', {
    'time_table': List[TrainType],
    'url': str
})

NavitimeParametersType = TypedDict('NavitimeParametersType', {
    'orvStationName': str,
    'orvStationCode': str,
    'dnvStationName': str,
    'dnvStationCode': str,
    'thr1StationName': str,
    'thr1StationCode': str,
    'thr2StationName': str,
    'thr2StationCode': str,
    'thr3StationName': str,
    'thr3StationCode': str,
    'year': str,
    'month': str,
    'day': str,
    'hour': str,
    'minute': str,
    'basis': str,
    'freePass': str,
    'sort': str,
    'wspeed': str,
})