from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

X = input().rstrip()
d = list(map(int, list(X)))
D = [d[0]]
for i in range(1, len(d)):
    D.append(D[i - 1] + d[i])
S = deque()
for i in range(len(D) - 1, -1, -1):
    S.appendleft(str(D[i] % 10))
    if i - 1 >= 0:
        D[i - 1] += D[i] // 10
    else:
        if D[i] // 10 != 0:
            S.appendleft(str(D[i] // 10))
print("".join(S))

