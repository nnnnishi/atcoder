from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, Q = [int(_) for _ in input().split()]
b = defaultdict(int)
a = defaultdict(int)

query = []
for _ in range(Q):
    query.append([int(_) for _ in input().split()])

for q in query:
    if q[0] == 1:
        a[q[1]] = q[2]
        b[q[2]] = q[1]
        if q[1] not in b:
            b[q[1]] = ""
    elif q[0] == 2:
        a[q[1]] = ""
        b[q[2]] = ""
    elif q[0] == 3:
        ans = []
        nx = q[1]
        if nx not in b:
            ans.append(nx)
        else:
            while b[nx] != "" and nx != b[nx]:
                nx = b[nx]
            ans.append(nx)
            while nx in a and a[nx] != "":
                nx = a[nx]
                ans.append(nx)
        print(len(ans), *ans)

