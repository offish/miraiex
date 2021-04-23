from requests import get


def floatify(data: dict) -> dict:
    response = {}

    for key in data:
        try:
            response[key] = float(data[key])
        except:
            pass

    return response


def get_request(uri: str, market: str = "", payload: dict = {}) -> dict:
    if market:
        uri = uri.format(market)

    try:
        return get(uri, params=payload).json()
    except:
        return {}


def types(*types):
    def check(f):
        assert len(types) == f.__code__.co_argcount

        def function(*args, **kwargs):
            for (a, t) in zip(args, types):
                if not isinstance(a, t):
                    raise TypeError(f"{a} must be {t.__name__}, not {type(a).__name__}")

            return f(*args, **kwargs)

        function.__name__ = f.__name__
        return function

    return check
