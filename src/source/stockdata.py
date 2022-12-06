# Interface for https://www.stockdata.org

import os
import pandas
import requests



API_EOD_URL = "https://api.stockdata.org/v1/data/eod"



def get_symbol(symbol, date_from=None, date_to=None, asc=True):
    params = {}
    params["api_token"] = os.environ["STOCK_API_TOKEN"]

    params["symbols"] = symbol
    params["sort"] = "asc" if asc else "desc"

    if date_from is not None:
        params["date_from"] = date_from
    if date_to is not None:
        params["date_to"] = date_to

    response = requests.get(API_EOD_URL, params=params)
    data = response.json()["data"]

    return pandas.DataFrame(data=data)
