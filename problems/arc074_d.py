from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
a = [int(_) for _ in input().split()]

# 左
l = a[:N].copy()
suml = sum(l)
heapify(l)
v = heappop(l)
L = [suml]
for k in range(N, 2 * N):
    if v < a[k]:
        suml += a[k] - v
        heappush(l, a[k])
        v = heappop(l)
        L.append(suml)
    else:
        L.append(suml)

# 右
r = a[2 * N :].copy()
sumr = sum(r)
rm = [-x for x in r]
heapify(rm)
v = heappop(rm)
R = [sumr]
for k in range(2 * N - 1, N - 1, -1):
    if v < -a[k]:
        sumr += a[k] + v
        heappush(rm, -a[k])
        v = heappop(rm)
        R.append(sumr)
    else:
        R.append(sumr)

ans = -(10 ** 30)

for i in range(N + 1):
    ans = max(ans, L[i] - R[N - i])
print(ans)