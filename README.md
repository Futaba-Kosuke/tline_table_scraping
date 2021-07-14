# tline_table_scraping

時刻表管理LINEボット「**TLi;NE TABLE**」のスクレイピングサーバーです。

## Specification

### inputs

```sh
{
    'starting_point': '{$現在駅}'
    'end_point': '{$目的駅}'
}

# example
{
    'starting_point': '田川後藤寺'
    'end_point': '小倉'
}
```

### outputs

```sh
{
    'time_table': [
        { 'time': ['HH:MM', 'HH:MM'], 'type': 'local', 'transfer': 0 },
        { 'time': ['HH:MM', 'HH:MM'], 'type': 'rapid', 'transfer': 1 },
        { 'time': ['HH:MM', 'HH:MM'], 'type': 'regional_rapid', 'transfer': 2 },
        ...
    ],
    'url': 'URL'
}

# example
{
    'time_table': [
        { 'time': ['07:18', '08:24'], 'type': 'local', 'transfer': 0 },
        { 'time': ['07:35', '08:33'], 'type': 'rapid', 'transfer': 0 },
        { 'time': ['08:06', '09:02'], 'type': 'local', 'transfer': 1 },
        ...
    ],
    'url': 'https://www.navitime.co.jp/transfer/searchlist?orvStationName=%E7%94%B0%E5%B7%9D%E5%BE%8C%E8%97%A4%E5%AF%BA&orvStationCode=&dnvStationName=%E5%B0%8F%E5%80%89&dnvStationCode=&thr1StationName=&thr1StationCode=&thr2StationName=&thr2StationCode=&thr3StationName=&thr3StationCode=&year=2021&month=7&day=14&hour=12&minute=12&basis=1&freePass=0&sort=4&wspeed=100&airplane=1&sprexprs=1&utrexprs=1&othexprs=1&mtrplbus=1&intercitybus=1&ferry=1'
}
```

## Requirements

- python 3.9.6

## Installation

```sh
# Clone
git clone git@github.com:Futaba-Kosuke/tline_table_scraping.git
cd tline_table_scraping

# (optional) Build the virtual environment
python -m venv .env
source .env/bin/activate

# Install modules
python -m pip install -r requirements.txt
```

## Usage

```sh
# Start the uvicorn server
uvicorn main:app --reload
```
