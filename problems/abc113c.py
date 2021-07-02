from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = list(map(int, input().split()))
L = []
for i in range(N):
    K = [int(_) for _ in input().split()]
    L += K[1:]
l = Counter(L)
ans = 0
for k, v in l.most_common():
    if v == N:
        ans += 1
    else:
        break
print(ans)
