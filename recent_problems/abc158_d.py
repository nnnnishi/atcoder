from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations


S = input()
q = deque(list(S))
Q = int(input())
inv = False
for _ in range(Q):
    X = [_ for _ in input().split()]
    if X[0] == "1":
        if inv:
            inv = False
        else:
            inv = True
    else:
        if X[1] == "1":
            if inv:
                q.append(X[2])
            else:
                q.appendleft(X[2])
        else:
            if inv:
                q.appendleft(X[2])
            else:
                q.append(X[2])
if inv:
    print("".join(list(q)[::-1]))
else:
    print("".join(q))
