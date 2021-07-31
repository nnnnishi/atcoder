N = int(input())
M = 10 ** 9 + 7
A = [[int(_) for _ in input().split()] for i in range(N)]
ans = 1
for i in range(N):
    ans *= sum(A[i])
    ans %= M
print(ans)