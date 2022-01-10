import sys

input = sys.stdin.readline
N = int(input())
A = [int(_) for _ in input().split()]
ans = 0
for i in range(N):
    ans += A[i] * i - A[i] * (N - 1 - i)
print(ans)
