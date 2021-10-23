from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

S = list(input())

d = defaultdict(int)

if len(S) == 2:
    if S[0] == S[1]:
        print("NO")
    else:
        print("YES")
    exit()

for s in S:
    d[s] += 1

c = []
for k, v in d.items():
    c.append([v, k])
c.sort(reverse=True)

if (len(S) - c[0][0]) // 2 >= c[0][0] - 1:
    print("YES")
else:
    print("NO")
