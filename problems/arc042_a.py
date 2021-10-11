from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = [int(_) for _ in input().split()]
s = set()
done = set()
q = deque()
for i in range(M):
    q.appendleft(int(input()))

for _ in range(M):
    i = q.popleft()
    if i not in done:
        print(i)
        done.add(i)
for i in range(1, N + 1):
    if i not in done:
        print(i)

