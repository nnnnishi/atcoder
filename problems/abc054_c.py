from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = [int(_) for _ in input().split()]
p = set()
for i in range(M):
    a, b = [int(_) for _ in input().split()]
    if b >= a:
        p.add((a - 1, b - 1))
    else:
        p.add((b - 1, a - 1))
ans = 0
for pi in permutations(range(1, N), N - 1):
    pi = [0] + list(pi)
    ok = True
    for i in range(N - 1):
        a = pi[i]
        b = pi[i + 1]

        if b >= a:
            if (a, b) not in p:
                ok = False
                break
        else:
            if (b, a) not in p:
                ok = False
                break
    if ok:
        ans += 1
print(ans)