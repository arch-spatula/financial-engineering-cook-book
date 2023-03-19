
from pykrx import stock

tickers = stock.get_market_ticker_list("20190225")

print(tickers)