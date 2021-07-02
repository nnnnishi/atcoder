from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

M, N = [int(_) for _ in input().split()]
K = int(input())
A = []
for k in range(M):
    A.append(list(input()))
Q = []
for k in range(K):
    Q.append([int(_) for _ in input().split()])

# 二次元累積和
sumX = {}
for s in ["J", "O", "I"]:
    sumX[s] = [[0] * (N + 1)]
    for i in range(M):
        sumX[s].append([0] * (N + 1))

for y in range(1, M + 1):
    for x in range(1, N + 1):
        sa = A[y - 1][x - 1]
        for s in ["J", "O", "I"]:
            if s == sa:
                sumX[s][y][x] = (
                    sumX[s][y - 1][x] + sumX[s][y][x - 1] - sumX[s][y - 1][x - 1] + 1
                )
            else:
                sumX[s][y][x] = (
                    sumX[s][y - 1][x] + sumX[s][y][x - 1] - sumX[s][y - 1][x - 1]
                )
for q in Q:
    y1, x1, y2, x2 = q
    for s in ["J", "O", "I"]:
        # J
        ans = (
            sumX[s][y2][x2]
            - sumX[s][y1 - 1][x2]
            - sumX[s][y2][x1 - 1]
            + sumX[s][y1 - 1][x1 - 1]
        )
        if s != "I":
            print(ans, end=" ")
        else:
            print(ans)
