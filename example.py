from miraiex import MiraiEx, RIPPLE, XRP, BITCOIN

miraiex = MiraiEx()

print(miraiex.get_time())
print(miraiex.get_markets())
print(miraiex.get_tickers())
print(miraiex.get_market("XRPNOK"))
print(miraiex.get_market_history(RIPPLE, 1))
print(miraiex.get_orderbook(XRP))
print(miraiex.get_orderbooks("BTCNOK"))
print(miraiex.get_market_ticker(BITCOIN))