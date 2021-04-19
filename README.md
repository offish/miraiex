# MiraiEx

[![Version](https://img.shields.io/pypi/v/miraiex.svg)](https://pypi.org/project/miraiex)
[![Stars](https://img.shields.io/github/stars/offish/miraiex.svg)](https://github.com/offish/miraiex/stargazers)
[![Issues](https://img.shields.io/github/issues/offish/miraiex.svg)](https://github.com/offish/miraiex/issues)
[![Size](https://img.shields.io/github/repo-size/offish/miraiex.svg)](https://github.com/offish/miraiex)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python package for interacting with [MiraiEx](https://miraiex.com/affiliate/?referral=01f67b69)' (refferal) [API](https://developers.miraiex.com/#/).

[MiraiEx](https://miraiex.com) (not refferal)

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
[{'id': 'BTCNOK', 'last': '473000.20', 'high': '533400.00', 'change': '-9.25', 'low': '460000.00', 'volume': '47.21'}, ...]
```

## Documentation
MiraiEx' official documentation can be found [here](https://developers.miraiex.com/#/README).
