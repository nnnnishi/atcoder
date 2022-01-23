from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = [int(_) for _ in input().split()]
S = [int(_) for _ in input().split()]
T = [int(_) for _ in input().split()]

if not set(T) <= set(S):
    print(-1)
    exit()

pos = S[0]
check = []
idx = 0
isFirst = True
ans = 0
for t in T:
    if t == pos:
        ans += 1
    else:
        if isFirst:
            for i, s in enumerate(S):
                if s == t:
                    check.append(i)
            mi = min(check)
            ma = len(S) - max(check)
            ans += min(mi, ma) + 1
            pos = (pos + 1) % 2
            isFirst = False
        else:
            ans += 2
            pos = (pos + 1) % 2

print(ans)
