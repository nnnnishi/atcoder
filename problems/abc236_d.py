import sys

input = sys.stdin.readline
N = int(input())
A = []
for i in range(2 * N - 1):
    A.append(list(map(int, input().split())))


def has_bit(n, i):
    return (n & 1 << i) > 0


dp = [0] * (1 << (2 * N))
print(A)
# おとずれた点の組合せ
for t in range(N):
    for n in range(1 << (2 * N)):
        cnt = 0
        for k in range(2 * N):
            if has_bit(n, k):
                cnt += 1
        # おとずれたのが2tでなければ飛ばす
        if cnt != 2 * t:
            continue
        print(n)
        # 前の点
        for i in range((2 * N) - 1):
            if has_bit(n, i):
                continue
            # つぎの点
            for j in range(i + 1, 2 * N):
                # すでに訪れていれば飛ばす
                if has_bit(n, j):
                    continue
                # 距離が小さくなる時、そのルートを保存
                if dp[n | (1 << i) | (1 << j)] < (dp[n] ^ A[i][j - i - 1]):
                    dp[n | (1 << i) | (1 << j)] = dp[n] ^ A[i][j - i - 1]
print(dp)
print(dp[(1 << (2 * N)) - 1])

