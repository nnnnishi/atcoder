from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
S = list(input())
q = deque()
q.append(N)
for i in range(N - 1, -1, -1):
    if S[i] == "L":
        q.append(i)
    else:
        q.appendleft(i)
print(*q)
