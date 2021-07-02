from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, K = list(map(int, input().split()))
A = [[int(_) for _ in input().split()] for i in range(N)]
if K % 2 == 0:
    medidx = (K ** 2) // 2
else:
    medidx = (K ** 2) // 2 + 1
# ある値より大きいかどうかの行列をつくる
def gen_mat(M):
    B = []
    sumB = []
    B.append([0] * (N + 1))
    for y in range(N):
        B.append([0] * (N + 1))
        for x in range(N):
            if A[y][x] <= M:
                B[y + 1][x + 1] = 1
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            B[y][x] = B[y][x] + B[y - 1][x] + B[y][x - 1] - B[y - 1][x - 1]
    for y1 in range(K, N + 1):
        for x1 in range(K, N + 1):
            num = B[y1][x1] - B[y1 - K][x1] - B[y1][x1 - K] + B[y1 - K][x1 - K]
            if num >= medidx:
                return True
    return False


# 二次元累積和
ng = -1
ok = 10 ** 9 + 1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if gen_mat(mid):
        ok = mid
    else:
        ng = mid
print(ok)
