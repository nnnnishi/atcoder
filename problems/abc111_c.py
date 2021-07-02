from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [int(_) for _ in input().split()]
la = []
lb = []
for i in range(len(A)):
    if i % 2 == 0:
        la.append(A[i])
    else:
        lb.append(A[i])
if len(set(la)) == len(set(lb)) == 1:
    if A[0] == A[1]:
        print(N // 2)
    else:
        print(0)
else:
    ca = Counter(la)
    cb = Counter(lb)

    if ca.most_common()[0][0] == cb.most_common()[0][0]:
        print(
            min(
                N - ca.most_common()[0][1] - cb.most_common()[1][1],
                N - cb.most_common()[0][1] - ca.most_common()[1][1],
            )
        )
    else:
        print(N - cb.most_common()[0][1] - ca.most_common()[0][1])
