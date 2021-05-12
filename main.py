import config, csv
from binance.client import Client
client = Client(config.API_KEY, config.API_SECRET)
from datetime import datetime


#prices = client.get_all_tickers()
#for price in prices:
#    print(price)

now = datetime.now()
today = now.strftime("%d/%m/%Y %H:%M:%S")
candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, "1 January, 2021", today)


csvfile = open('main.csv', 'w', newline='')
candelstick_writer = csv.writer(csvfile, delimiter=',')


for candle in candles:
    print(candle)
    candelstick_writer.writerow(candle)
print(len(candles)) 