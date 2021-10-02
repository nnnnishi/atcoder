from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
d = {}
for i in range(N):
    a, b = [int(_) for _ in input().split()]
    d.setdefault(a, 0)
    d.setdefault(a + b, 0)
    d[a] += 1
    d[a + b] -= 1
# print(d[a + b])
# print("d", d)
ks = []
for k in d.keys():
    ks.append(k)
ks.sort()
# print(ks)
nb = d[ks[0]]
kb = ks[0]
D = defaultdict(int)
for k in ks[1:]:
    D[nb] += k - kb
    # print("*", nb, k - kb)
    nb += d[k]
    kb = k

# print(D)
ans = []
for i in range(1, N + 1):
    ans.append(D[i])
print(*ans)
