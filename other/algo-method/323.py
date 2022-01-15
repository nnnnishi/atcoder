N, M = [int(_) for _ in input().split()]
D = [int(_) for _ in input().split()]
dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    for j in range(M):
        if i - D[j] >= 0 and dp[i - D[j]] == 1:
            dp[i] = 1
            break
if dp[N] == 1:
    print("Yes")
else:
    print("No")

