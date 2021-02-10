import requests
import json

r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
bitcoin = json.loads(r.text)
price = bitcoin['bitcoin']['usd']
print('Bitcoin current price is: ${}'.format(price))