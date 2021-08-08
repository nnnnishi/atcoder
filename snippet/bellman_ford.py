# ベルマンフォード (単一頂点最短路): O(EV)
# 負のコストがある、有向グラフ（負のコストがあり無向グラフだと往復で無限に減らせる）
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp
# 頂点数、枝数、始点
V, E, r = [int(_) for _ in input().split()]

G = []
for i in range(E):
    s, e, c = [int(_) for _ in input().split()]  # 始点,終点,コスト
    G.append([s, e, c])
    # G.append([s, e, c])  # 無向グラフは逆側もいれる


def bellman_ford(s):
    d = [float("inf")] * V  # 各頂点への最小コスト
    d[s] = 0  # 自身への距離は0
    for i in range(V):
        update = False  # 更新が行われたか
        # すべての辺をたどる
        for s, e, c in G:
            if d[s] + c < d[e]:
                d[e] = d[s] + c
                update = True
        if not update:
            break
        # V-1回以上更新できる場合は負閉路が存在
        if i == V - 1:
            exit(print("NEGATIVE CYCLE"))
    return d


for a in bellman_ford(r):
    if a == float("inf"):
        # たどりつけない
        print("INF")
    else:
        # たどりつけて、最短距離がある
        print(a)
