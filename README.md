# MiraiEx
Python package for interacting with [MiraiEx](https://miraiex.com)' API.

**THIS PACKAGE DOES NOT CURRENTLY SUPPORT PRIVATE ENDPOINTS.**

## Installation
Install and update using pip
```text
pip install --upgrade miraiex
```

## Usage
```python
>>> from miraiex import MiraiEx, BITCOIN, BTC
>>> miraiex = MiraiEx()
>>> miraiex.get_market(BITCOIN) # or get_prices(BTC) or "BTCNOK". Predefined tickers can be found in markets.py
{'last': '480408.40', 'high': '533400.00', 'change': '-7.77', 'low': '460000.00', 'volume': '46.86'}

>>> miraiex.get_markets() # or get_tickers()
[{'id': 'BTCNOK', 'last': '473000.20', 'high': '533400.00', 'change': '-9.25', 'low': '460000.00', 'volume': '47.21'}, {'id': 'DAINOK', 'last': '8.48', 'high': '8.87', 'change': '1.92', 'low': '8.33', 'volume': '38116.06'}, {'id': 'ETHNOK', 'last': '19854.80', 'high': '21286.41', 'change': '-3.1', 'low': '17316.79', 'volume': '449.21'}, {'id': 'LTCNOK', 'last': '2258.47', 'high': '2840.55', 'change': '-20.19', 'low': '2090.05', 'volume': '1541.88'}, {'id': 'XRPNOK', 'last': '11.61', 'high': '14.38', 'change': '-17.07', 'low': '9.96', 'volume': '1362611.64'}]
```

## Documentation
MiraiEx' official documentation can be found [here](https://developers.miraiex.com/#/).