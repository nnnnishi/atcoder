from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)


@lru_cache(maxsize=None)
def pow2(n, m):
    return pow(n, m)


N, M = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
b = [0] * N
suma = sum(a)


dis = []
for i in range(N):
    # 値引き額
    dis.append((-(a[i] - (a[i] // 2)), i))

heapify(dis)
dsum = 0
for i in range(M):
    c = heappop(dis)
    dsum += c[0]
    b[c[1]] += 1
    sa = a[c[1]] // pow2(2, b[c[1]] + 1) - (a[c[1]] // pow2(2, b[c[1]]))
    heappush(dis, (sa, c[1]))
print(suma + dsum)
