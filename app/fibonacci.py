"""
"""

from devutls.debug import trace
from functools import lru_cache


@trace
@lru_cache
def cache_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return cache_fibonacci(n - 1) + cache_fibonacci(n - 2)


def g_fibonacci(n):
    def generator():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    g = generator()
    for _ in range(n + 1):
        r = next(g)
    return r


if __name__ == '__main__':
    # fibb = cache_fibonacci(10)
    # print(fibb)

    print(g_fibonacci(100))
