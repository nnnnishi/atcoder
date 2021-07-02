import numpy as np

cdic = {"B": 0, "R": 1, "W": 2, "#": 3}
N = int(input())
C = []
for i in range(5):
    C.append(list(input()))
C = np.array(C).T
dp = [[0] * (N + 1) for _ in range(3)]
for i in range(1, N + 1):
    B = 0
    R = 0
    W = 0
    for s in C[i - 1]:
        if s == "B":
            B += 1
        elif s == "R":
            R += 1
        elif s == "W":
            W += 1
    for c in range(3):
        # cでないものですくないほう
        if c == 0:
            dp[c][i] = min(
                dp[(c - 1) % 3][i - 1] + (5 - W), dp[(c - 2) % 3][i - 1] + (5 - R)
            )
        elif c == 1:
            dp[c][i] = min(
                dp[(c - 1) % 3][i - 1] + (5 - B), dp[(c - 2) % 3][i - 1] + (5 - W)
            )
        elif c == 2:
            dp[c][i] = min(
                dp[(c - 1) % 3][i - 1] + (5 - R), dp[(c - 2) % 3][i - 1] + (5 - B)
            )
print(min(dp[0][N], dp[1][N], dp[2][N]))
