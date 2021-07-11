from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
a = [int(_) for _ in input().split()]
Q = deque()
Q.append(a[0])
if N == 1:
    exit(print(a[0]))
if N % 2 == 0:
    # ひだりから
    for i in range(1, N):
        if i % 2 != 0:
            Q.appendleft(a[i])
        else:
            Q.append(a[i])
else:
    # みぎから
    for i in range(1, N):
        if i % 2 != 0:
            Q.append(a[i])
        else:
            Q.appendleft(a[i])
print(*Q)