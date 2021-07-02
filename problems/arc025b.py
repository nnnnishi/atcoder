import copy
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

H, W = [int(_) for _ in input().split()]
A = [[0] * (W + 1)] + [[0] + [int(_) for _ in input().split()] for i in range(H)]
BL = copy.deepcopy(A)
WH = copy.deepcopy(A)
for x in range(1, W + 1):
    for y in range(1, H + 1):
        if (x + y) % 2 == 0:
            WH[y][x] = 0
        else:
            BL[y][x] = 0
# print(WH)
# print(BL)
# すべての累積和
for y in range(1, H + 1):
    for x in range(1, W + 1):
        WH[y][x] = WH[y][x] + WH[y - 1][x] + WH[y][x - 1] - WH[y - 1][x - 1]
        BL[y][x] = BL[y][x] + BL[y - 1][x] + BL[y][x - 1] - BL[y - 1][x - 1]

# 左上と右下をきめれば全長方形領域が列挙できる
ans = 0
for y1 in range(H + 1):
    for x1 in range(W + 1):
        for y2 in range(y1, H + 1):
            for x2 in range(x1, W + 1):
                sumWH = WH[y2][x2] - WH[y1][x2] - WH[y2][x1] + WH[y1][x1]
                sumBL = BL[y2][x2] - BL[y1][x2] - BL[y2][x1] + BL[y1][x1]
                # print(sumWH, sumBL)
                S = (x2 - x1) * (y2 - y1)
                if sumWH == sumBL:
                    ans = max(S, ans)
print(ans)