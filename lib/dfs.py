from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
