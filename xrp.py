# not working

import sys, requests, bs4

xrp_coins = 701.145288
usd_used = 302.71

res = requests.get('https://coinmarketcap.com/es/currencies/xrp/')
res.raise_for_status()
coinmarketcap_soup = bs4.BeautifulSoup(res.text, 'html.parser')
element = coinmarketcap_soup.findAll("span", {"class": "cmc-details-panel-price__price"})
element_data = element[0].getText()
current_price = float(element_data[1:])

at_price = usd_used / xrp_coins
xrp_on_usd = xrp_coins * current_price

print('XRP Coins: {:.2f}'.format(xrp_coins))
print('XRP Current Price: ${:.2f}'.format(current_price))
print('XRP on USD: ${:.2f}'.format(xrp_on_usd))

if xrp_on_usd > usd_used:
    profit = xrp_on_usd - usd_used
    print('Profit: ${:.2f}'.format(profit))
else:
    losses = usd_used - xrp_on_usd
    print('Losses: ${:.2f}'.format(losses))

sys.exit()