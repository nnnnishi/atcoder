# 巡回セールスマン問題 O(N^2*2^N)
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_c
N = int(input())
A = []
for i in range(N):
    A.append([int(_) for _ in input().split()])


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
