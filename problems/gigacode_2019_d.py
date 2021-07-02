from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

H, W, K, V = [int(_) for _ in input().split()]
A = [[0] * (W + 1)] + [[0] + [int(_) for _ in input().split()] for i in range(H)]

for y in range(1, H + 1):
    for x in range(1, W + 1):
        A[y][x] = A[y][x] + A[y - 1][x] + A[y][x - 1] - A[y - 1][x - 1]

# 左上と右下をきめれば全長方形領域が列挙できる
ans = 0
for y1 in range(H + 1):
    for x1 in range(W + 1):
        for y2 in range(y1, H + 1):
            for x2 in range(x1, W + 1):
                sumA = A[y2][x2] - A[y1][x2] - A[y2][x1] + A[y1][x1]
                S = (x2 - x1) * (y2 - y1)
                if sumA + K * S <= V:
                    ans = max(S, ans)
print(ans)