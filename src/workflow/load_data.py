import datetime
import json
import os
import time



from ..source import stockdata



PERIODS = {
    '1mo': datetime.timedelta(weeks=4),
    '3mo': datetime.timedelta(weeks=13),
    '1yr': datetime.timedelta(weeks=52),
    '5yr': datetime.timedelta(weeks=260)
}

STOCK_PATH = "/data/stocks"



def load_stocks(path):
    symbols = {}

    for filename in os.listdir(path):
        with open(f"{path}/{filename}") as file:
            spec = json.load(file)
        symbols[spec["symbol"]] = spec
    
    return symbols


def run():
    as_of = os.environ.get("STOCK_AS_OF", None)
    if as_of is not None:
        year, month, day = [int(x) for x in as_of.split("-")]
        today = datetime.date(year=year, month=month, day=day)
    else:
        today = datetime.date.today()

    symbols = load_stocks(STOCK_PATH)

    data = {}
    for period, delta in PERIODS.items():
        start_date = today - delta
        
        data[period] = {}
        for symbol in symbols:    
            data[period][symbol] = stockdata.get_symbol(symbol, date_from=start_date, date_to=today)
        
        time.sleep(60)

    return (symbols, data)
