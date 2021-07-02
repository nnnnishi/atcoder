N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
A.sort()
ans = 0
for i in range(K):
    ans = (ans + A[N - K + i]) / 2
print(ans)