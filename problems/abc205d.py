from fractions import gcd
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = []
for i in range(N):
    B.append(A[i] - (i + 1))
for _ in range(Q):
    K = int(input())
    if K <= B[0]:
        print(K)
    elif K > B[N - 1]:
        print(K - B[N - 1] + A[N - 1])
    else:
        idx = bisect_left(B, K)
        print(A[idx] - (B[idx] - K) - 1)
