# 巡回セールスマン問題 O(N^2*2^N)
# 駅伝型 -> Nが小さければ全列挙で解ける
# https://atcoder.jp/contests/typical90/tasks/typical90_af
N = int(input())
A = []
for i in range(N):
    A.append([int(_) for _ in input().split()])
M = int(input())

ng = set()
for _ in range(M):
    x, y = [int(_) for _ in input().split()]
    ng.add((x - 1, y - 1))
    ng.add((y - 1, x - 1))


def has_bit(n, i):
    return (n & 1 << i) > 0


def popcount(x):
    """xの立っているビット数をカウントする関数
    https://qiita.com/zawawahoge/items/8bbd4c2319e7f7746266
    (xは64bit整数)"""

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0F0F0F0F0F0F0F0F  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007F


INF = 10 ** 10
# cost[走ったひとの状態][最後に走った人] = min(cost[走ったひとの状態][最後に走った人], cost[走ったひとの状態][まえ最後に走った人] + A[その人][bitの数])
cost = [[INF] * N for _ in range(1 << N)]
# 0を始点とする
for i in range(N):
    cost[0][i] = 0

for n in range(1 << N):
    if n == 0:
        for j in range(N):
            cost[n | (1 << j)][j] = A[j][0]
    else:
        for i in range(N):
            for j in range(N):
                # すでに訪れているとき、前と一緒、ダメな組合せ
                if has_bit(n, j) or not has_bit(n, i) or (i, j) in ng:
                    continue
                # 距離が小さくなる時、そのルートを保存
                cost[n | (1 << j)][j] = min(
                    cost[n | (1 << j)][j], cost[n][i] + A[j][popcount(n)]
                )
# 最後にたどり着いたときのコスト
ans = min(cost[(1 << N) - 1])
if ans != INF:
    print(ans)
else:
    print(-1)
