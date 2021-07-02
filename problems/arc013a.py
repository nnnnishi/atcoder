from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations


A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
ans = 0
for p in [v for v in permutations([0, 1, 2], 3)]:
    a = 1
    for i, j in zip([0, 1, 2], p):
        a *= A[i] // B[j]
    ans = max(a, ans)
print(ans)
