

from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        print_yellow(f'{func.__name__}({args}, {kwargs}) -> {output}')
        return output
    return wrapper
