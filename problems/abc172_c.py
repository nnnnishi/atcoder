from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
sumA = [0] * (N + 1)
sumB = [0] * (M + 1)
sumA[0] = 0
sumB[0] = 0
for i in range(1, N + 1):
    sumA[i] = sumA[i - 1] + A[i - 1]
for i in range(1, M + 1):
    sumB[i] = sumB[i - 1] + B[i - 1]
# Aを固定してBはいけるだけいく
ans = 0
for i in range(N + 1):
    cnt = 0
    if sumA[i] <= K:
        res = K - sumA[i]
        cnt += i
        j = bisect_right(sumB, res) - 1
        cnt += j
        ans = max(ans, cnt)
    else:
        break
print(ans)