# 巡回セールスマン問題 O(N^2*2^N)
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_c
N = int(input())
A = []
for i in range(N):
    A.append([int(_) for _ in input().split()])


def has_bit(n, i):
    return (n & 1 << i) > 0


INF = 10 ** 10
# cost[訪問した集合][前の点] -> 次の点が訪問した集合に含まれていないか確認しつつ、前の点からコストを計算する
cost = [[INF] * N for _ in range(1 << N)]

# 0を始点とする
cost[0][0] = 0

# おとずれた点の組合せ
for n in range(1 << N):
    # 前の点
    for i in range(N):
        # つぎの点
        for j in range(N):
            # すでに訪れている、または前と一緒のとき、とばす
            if has_bit(n, j) or i == j:
                continue
            # 距離が小さくなる時、そのルートを保存
            cost[n | (1 << j)][j] = min(cost[n | (1 << j)][j], cost[n][i] + A[i][j])

# 0にもどってきたときのコスト
print(cost[(1 << N) - 1][0])
