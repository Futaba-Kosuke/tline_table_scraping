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
        { 'time': ['HH:MM', 'HH:MM'], 'type': 'local' },
        { 'time': ['HH:MM', 'HH:MM'], 'type': 'rapid' },
        { 'time': ['HH:MM', 'HH:MM'], 'type': 'regional_rapid' },
        ...
    ]
}

# example
{
    'time_table': [
        { 'time': ['07:18', '08:24'], 'type': 'local' },
        { 'time': ['07:35', '08:33'], 'type': 'rapid' },
        { 'time': ['08:06', '09:02'], 'type': 'local' },
        ...
    ]
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
# Start the server
python server.py
```
