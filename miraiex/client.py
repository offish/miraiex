from .endpoints import *
from .utils import *


class MiraiEx:
    def get_time(self) -> dict:
        return get_request(TIME)

    def get_markets(self) -> dict:
        return get_request(MARKETS)

    def get_tickers(self) -> dict:
        return self.get_markets()

    @types(str)
    def get_market(self, market: str) -> dict:
        return get_request(MARKET, market)

    def get_prices(self, market: str) -> dict:
        return self.get_market(market)

    @types(str, int)
    def get_market_history(self, market: str, count: int = 0) -> dict:
        payload = {"count": count} if count else {}
        return get_request(HISTORY, market, payload=payload)

    @types(str)
    def get_orderbook(self, market: str) -> dict:
        return get_request(ORDERBOOKS, market)

    def get_orderbooks(self, market: str) -> dict:
        return self.get_orderbook(market)

    @types(str)
    def get_market_ticker(self, market: str) -> dict:
        return get_request(TICKER, market)