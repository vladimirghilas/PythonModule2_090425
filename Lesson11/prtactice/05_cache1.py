def cache(func):
    _cache = {}

    def wrapper(*args, **kwargs):
        key = args, tuple(sorted(kwargs.items()))
        if key in _cache:
            print(_cache)
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        print(_cache)
        return result

    return wrapper

@cache
def expencive_calc(n, m=1):
    return n*m
print(expencive_calc(5))
