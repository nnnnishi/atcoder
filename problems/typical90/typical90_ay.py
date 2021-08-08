from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, K, P = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

h = N // 2
r = N - h


def has_bit(n, i):
    return (n & 1 << i) > 0


# N桁の0-1の組合せパターン数 1<<N

d_k_tot = [[] for _ in range(h + 1)]
for n in range(1 << h):
    tot = 0
    cnt = 0
    # N桁
    for i in range(h):
        # パターンnのi桁目が1
        if has_bit(n, i):
            tot += a[i]
            cnt += 1
    if cnt <= K:
        d_k_tot[cnt].append(tot)

for i in range(h + 1):
    d_k_tot[i].sort()
# print(d_k_tot)

ans = 0
for n in range(1 << r):
    tot = 0
    cnt = 0
    # N桁
    for i in range(r):
        # パターンnのi桁目が1
        if has_bit(n, i):
            tot += a[h + i]
            cnt += 1
    if cnt <= K and 0 <= K - cnt <= h:
        ans += bisect_right(d_k_tot[K - cnt], P - tot)

print(ans)