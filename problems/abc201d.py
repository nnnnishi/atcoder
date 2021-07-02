H, W = list(map(int, input().split()))
A = []
dp = []
for i in range(H):
    tmpA = list(input())
    A.append([int(j + "1") for j in tmpA])
    dp.append([0] * W)

# h+w:even-> takahashi +
# h+w:odd -> aoki -

for h in range(H - 1, -1, -1):
    for w in range(W - 1, -1, -1):
        # みぎ　した
        if w <= W - 2 and h <= H - 2:
            if (h + w) % 2 == 0:
                dp[h][w] = max(dp[h + 1][w] + A[h + 1][w], dp[h][w + 1] + A[h][w + 1])
            else:
                dp[h][w] = min(dp[h + 1][w] - A[h + 1][w], dp[h][w + 1] - A[h][w + 1])
        # みぎ
        elif w <= W - 2 and h == H - 1:
            if (h + w) % 2 == 0:
                dp[h][w] = dp[h][w + 1] + A[h][w + 1]
            else:
                dp[h][w] = dp[h][w + 1] - A[h][w + 1]
        elif w == W - 1 and h <= H - 2:
            if (h + w) % 2 == 0:
                dp[h][w] = dp[h + 1][w] + A[h + 1][w]
            else:
                dp[h][w] = dp[h + 1][w] - A[h + 1][w]
        else:
            # りょうほうかべ
            dp[h][w] = 0
if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] < 0:
    print("Aoki")
else:
    print("Draw")