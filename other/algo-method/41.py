import sys

input = sys.stdin.readline
N = int(input())
A = [[int(_) for _ in input().split()] for _ in range(N)]
for i in range(1, N):
    for j in range(3):
        maxA = 0
        for k in range(3):
            if j != k:
                maxA = max(maxA, A[i - 1][k])
        A[i][j] += maxA

print(max(A[N - 1]))

