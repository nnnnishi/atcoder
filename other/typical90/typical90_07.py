from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [int(_) for _ in input().split()]
A.sort()
Q = int(input())
for _ in range(Q):
    B = int(input())
    idx = bisect(A, B)

    if idx == 0:
        ans = abs(B - A[0])
    elif idx == N:
        ans = abs(B - A[N-1])
    else:
        ans = min(abs(B - A[idx - 1]), abs(B - A[idx]))
    print(ans)
