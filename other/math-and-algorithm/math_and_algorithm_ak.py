N = int(input())
A = [0] + [int(_) for _ in input().split()]

for i in range(2, N):
    A[i] += A[i - 1]

M = int(input())
pre = int(input())
ans = 0
for i in range(M - 1):
    nx = int(input())
    ans += abs(A[nx - 1] - A[pre - 1])
    pre = nx
print(ans)
