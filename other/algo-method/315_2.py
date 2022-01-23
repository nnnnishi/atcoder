# レーベンシュタイン距離
# https://algo-method.com/tasks/314/editorial

import sys
from functools import lru_cache

input = sys.stdin.readline

S = input()
T = input()

sys.setrecursionlimit(1000000)


@lru_cache(maxsize=None)
def ld(s, t):
    if not s:
        return len(t)
    if not t:
        return len(s)
    if s[0] == t[0]:
        return ld(s[1:], t[1:])
    l1 = ld(s, t[1:])
    l2 = ld(s[1:], t)
    l3 = ld(s[1:], t[1:])
    return 1 + min(l1, l2, l3)


print(ld(S, T))

