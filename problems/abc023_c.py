from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

R, C, K = [int(_) for _ in input().split()]
N = int(input())
y = [0] * R
x = [0] * C
rd = defaultdict(int)
cd = defaultdict(int)
check = []
for i in range(N):
    r, c = [int(_) for _ in input().split()]
    y[r - 1] += 1
    x[c - 1] += 1
    check.append([r - 1, c - 1])

for i in range(R):
    rd[y[i]] += 1

for i in range(C):
    cd[x[i]] += 1

ans = 0
for k in range(K + 1):
    ans += rd[k] * cd[K - k]


# その場にあめがある
for r, c in check:
    if y[r] + x[c] == K:
        ans -= 1
    if y[r] + x[c] == K + 1:
        ans += 1

print(ans)