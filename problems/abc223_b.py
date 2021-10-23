from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

S = list(input())
q = deque(S)
all = []
for i in range(len(S) + 1):
    a = q.popleft()
    q.append(a)
    all.append("".join(q))

all.sort()
print(all[0])
print(all[-1])
