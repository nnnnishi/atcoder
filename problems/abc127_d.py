from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
d = defaultdict(int)
l = []
k = []
for i in range(M):
    b, c = [int(_) for _ in input().split()]
    d[c] += b
for ai in a:
    d[ai] += 1
l = [k for k in d.keys()]
l.sort(reverse=True)

i = 0
cnt = 0
ans = 0
while cnt < N:

    if d[l[i]] + cnt < N:
        cnt += d[l[i]]
        ans += l[i] * d[l[i]]
    else:
        ans += l[i] * (N - cnt)
        cnt += N - cnt

    i += 1
print(ans)
