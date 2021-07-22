# 再帰用
import sys

sys.setrecursionlimit(1000000)

N, P, Q = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
for i in range(N):
    A[i] %= P

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    if A[i] * A[j] % P * A[k] % P * A[l] % P * A[m] % P == Q:
                        ans += 1
