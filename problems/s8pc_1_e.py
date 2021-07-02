from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, Q = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
A = [0]
c = [1] + [int(_) for _ in input().split()] + [1]
M = (10 ** 9) + 7
ans = 0

# 　累積和
for i in range(N - 1):
    A.append(pow(a[i], a[i + 1], M))
sumA = list(accumulate(A))
for i in range(Q + 1):
    ans += abs(sumA[c[i] - 1] - sumA[c[i + 1] - 1]) % M
    ans %= M
print(ans)