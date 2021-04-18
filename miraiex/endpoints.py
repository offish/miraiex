URL = "https://api.miraiex.com/"
API = URL + "v2/"

# no version
TIME = URL + "time"

# version 2
# public
MARKETS = API + "markets"
MARKET = MARKETS + "/{}"
TICKERS = MARKETS + "/tickers"

TICKER = MARKET + "/ticker"
HISTORY = MARKET + "/history"
ORDERBOOKS = MARKET + "/depth"

# private
# tba