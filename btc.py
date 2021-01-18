usd = 250
btc_price_at_buy = 35000
btc_actual_price = 40000
new_usd = (usd * btc_actual_price) / btc_price_at_buy
new_usd = round(new_usd, 2)
print(new_usd)

goal_usd = 1000
btc_price_to_goal = (goal_usd * btc_price_at_buy) / usd
btc_price_to_goal = round(btc_price_to_goal, 2)
print(btc_price_to_goal)