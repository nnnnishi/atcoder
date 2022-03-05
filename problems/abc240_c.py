N, X = [int(_) for _ in input().split()]
dp = [[False] * (X + 1) for _ in range(N + 1)]
dp[0][0] = True
for n in range(N):
    a, b = [int(_) for _ in input().split()]
    for i in range(X + 1):
        if dp[n][i]:
            if i + a <= X:
                dp[n + 1][i + a] = True
            if i + b <= X:
                dp[n + 1][i + b] = True

if dp[N][X]:
    print("Yes")
else:
    print("No")

