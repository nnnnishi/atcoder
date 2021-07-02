N = int(input())
T = list(map(int, input().split()))
if N == 1:
    exit(print(T[0]))
ALL = (10 ** 5) + 1001
dp = [[False] * (ALL + 1) for i in range(N + 2)]
dp[0][0] = True
for idx in range(N + 1):
    for n in range(ALL):
        if dp[idx][n]:
            dp[idx + 1][n + T[idx - 1]] = True
            dp[idx + 1][n] = True

sumT = sum(T)
for i in range(-(-sumT // 2), ALL):
    if dp[N + 1][i]:
        exit(print(i))
