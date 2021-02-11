import requests
import json
import numpy as np
import pandas as pd
import time

date = int(time.time())
a_year_before = date - 31556926

btc_request = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from={a_year_before}&to={date}'

r = requests.get(btc_request)

database = r.json()

prices = np.array(database['prices'])

price_series = pd.Series(prices[:][1])

print(price_series)