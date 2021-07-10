A, B = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
dp = [[0] * (B + 1) for _ in range(A + 1)]

dp[A][B] = 0
for i in range(A - 1, -1, -1):
    print(i)
    if i == A - 1:
        # aは0,bをすすめる
        for j in range(B - 1, -1, -1):
            if (i + j) % 2 != 0:
                dp[i][j - 1] = dp[i][j] + b[j - 1]
            else:
                dp[i][j - 1] = dp[i][j]
    else:
        for j in range(B - 1, -1, -1):
            if j == B - 1:
                # bは0,aをすすめる
                if (i + j) % 2 != 0:
                    print("here")
                    dp[i - 1][j] = dp[i][j] + a[i - 1]
                else:
                    dp[i - 1][j] = dp[i][j]
            else:
                if (i + j) % 2 != 0:
                    dp[i - 1][j - 1] = max(
                        dp[i][j - 1] + b[j - 1], dp[i - 1][j] + a[i - 1]
                    )
                else:
                    dp[i - 1][j - 1] = min(dp[i - 1][j], dp[i][j - 1])
print(dp)
print(dp[A][B])
