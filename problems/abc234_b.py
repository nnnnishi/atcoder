import sys
import math

input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        d = math.sqrt((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2)
        if d > ans:
            ans = d
print(ans)
