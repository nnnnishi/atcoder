from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations


# Nが小さい
def cmb_sml(n, r):
    nCr = {}
    if r == 0 or r == n:
        return 1
    if r == 1:
        return n
    if (n, r) in nCr:
        return nCr[(n, r)]
    nCr[(n, r)] = cmb(n - 1, r) + cmb(n - 1, r - 1)
    return nCr[(n, r)]


N = int(input())
l = []

for i in range(N):
    S = input()
    if S[0] in ["M", "A", "R", "C", "H"]:
        l.append(S[0])
c = Counter(l)

if len(c) <= 2:
    print(0)
else:
    a = []
    ans = 0
    for k in c.keys():
        a.append(c[k])
    for c in combinations(a, 3):
        ans += c[0] * c[1] * c[2]
    print(ans)