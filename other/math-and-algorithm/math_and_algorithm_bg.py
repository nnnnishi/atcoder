import sys

input = sys.stdin.readline
M = 10 ** 9 + 7
N = int(input())
A = [int(_) for _ in input().split()]
A.sort()
ans = 0
for i in range(N):
    ans += A[i] * pow(2, i, M)
    ans %= M
print(ans)
