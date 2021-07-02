from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = [int(_) for _ in input().split()]
d = []
a = []
for i in range(N - 1):
    d.append(int(input()))
for i in range(M):
    a.append(int(input()))

# 累積和
sumD = [0] + list(accumulate(d))
# start
pos = 0
ans = 0
for ai in a:
    ans += abs(sumD[pos + ai] - sumD[pos])
    ans %= 10 ** 5
    pos += ai
print(ans)