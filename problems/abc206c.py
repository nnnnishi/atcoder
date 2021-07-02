from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)
ans = (N * (N - 1)) // 2
for i in c.values():
    if i > 1:
        ans -= (i * (i - 1)) // 2
print(ans)
