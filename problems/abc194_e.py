from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

d = defaultdict(int)
for i in range(M):
    d[a[i]] += 1
ans = 0
for i in range(M + 1):
    if d[i] == 0:
        ans = i
        break
q = deque(a[:M])

for i in range(M, N):
    e = q.popleft()
    d[e] -= 1
    d[a[i]] += 1
    q.append(a[i])
    if d[e] == 0 and e < ans:
        ans = e
print(ans)