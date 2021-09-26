N = int(input())
X, Y = [int(_) for _ in input().split()]

dp = [[1000] * ((Y + 1) * X + Y + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    A, B = [int(_) for _ in input().split()]
    for x in range(X + 1):
        for y in range(Y + 1):
            if dp[i][(Y + 1) * x + y] != 1000:
                if x + A >= X and y + B >= Y:
                    dp[i + 1][(Y + 1) * X + Y] = min(
                        dp[i + 1][(Y + 1) * X + Y], dp[i][(Y + 1) * x + y] + 1
                    )
                elif x + A >= X:
                    dp[i + 1][((Y + 1) * X) + y + B] = min(
                        dp[i + 1][(Y + 1) * X + y + B], dp[i][(Y + 1) * x + y] + 1
                    )
                elif y + B >= Y:
                    dp[i + 1][(Y + 1) * (x + A) + Y] = min(
                        dp[i + 1][(Y + 1) * (x + A) + Y], dp[i][(Y + 1) * x + y] + 1
                    )
                else:
                    dp[i + 1][(Y + 1) * (x + A) + (y + B)] = min(
                        dp[i + 1][(Y + 1) * (x + A) + (y + B)],
                        dp[i][(Y + 1) * x + y] + 1,
                    )
                dp[i + 1][(Y + 1) * x + y] = min(
                    dp[i][(Y + 1) * x + y], dp[i + 1][(Y + 1) * x + y]
                )

ans = dp[N][(Y + 1) * X + Y]
if ans == 1000:
    print(-1)
else:
    print(ans)
