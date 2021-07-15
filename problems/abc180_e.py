N = int(input())
d = []
for i in range(N):
    d.append([int(_) for _ in input().split()])


def calc(d1, d2):
    return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1]) + max(0, d2[2] - d1[2])


A = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] = calc(d[i], d[j])


def has_bit(n, i):
    return (n & 1 << i) > 0


INF = 10 ** 10
dp = [[INF] * N for _ in range(1 << N)]
dp[0][0] = 0
for n in range(1 << N):
    for i in range(N):
        for j in range(N):
            if has_bit(n, j) or i == j:
                continue
            dp[n | (1 << j)][j] = min(dp[n | (1 << j)][j], dp[n][i] + A[i][j])
print(dp[(1 << N) - 1][0])
