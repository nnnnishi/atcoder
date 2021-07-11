from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
a = [int(_) for _ in input().split()]
suma = sum(a)
cnt = 0
ans = 10 ** 20
m = 0
for i in range(N - 1):
    m += a[i]
    suma -= a[i]
    ans = min(abs(suma - m), ans)
print(ans)