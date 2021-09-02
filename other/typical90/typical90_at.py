from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
M = 46
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
C = [int(_) for _ in input().split()]
for i in range(N):
    A[i] = A[i] % M
    B[i] = B[i] % M
    C[i] = C[i] % M
ac = Counter(A)
bc = Counter(B)
cc = Counter(C)

ans = 0
for ak in ac.keys():
    for bk in bc.keys():
        if (M - ((ak + bk) % M)) % M in cc:
            ans += ac[ak] * bc[bk] * cc[(M - ((ak + bk) % M)) % M]
print(ans)
