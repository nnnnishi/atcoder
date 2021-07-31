from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [int(_) for _ in input().split()]
A.sort()
Q = int(input())
qq = []
for _ in range(Q):
    qq.append(int(input()))
for q in qq:
    i = bisect_left(A, q)
    if i <= 0:
        print(abs(A[0] - q))
    elif i >= N:
        print(abs(A[N - 1] - q))
    else:
        print(min(abs(A[i - 1] - q), abs(A[i] - q)))
