# 強連結成分分解(Strongly Connected Components: SCC): グラフGに対するSCCを行う
# https://atcoder.jp/contests/typical90/tasks/typical90_u
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/021.jpg

import sys

sys.setrecursionlimit(1000000)


def scc(N, G, RG):
    """
    入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
    出力: (<ラベル数>, <各頂点のラベル番号>)
    """
    order = []
    used = [0] * N
    group = [None] * N

    def dfs(s):
        used[s] = 1
        # 順方向の有向グラフ
        for t in G[s]:
            if not used[t]:
                dfs(t)
        # でてきたときにsを足す（帰りがけ順）
        order.append(s)

    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        # 逆方向の有向グラフ
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)

    for i in range(N):
        # dfsでたどれてないところがあればたどる（連結でないグラフ）
        if not used[i]:
            dfs(i)

    used = [0] * N
    label = 0
    # 帰りがけ順の逆からたどる
    for s in reversed(order):
        if not used[s]:
            # rdfsで0からラベル付けする
            rdfs(s, label)
            label += 1
    # ラベルと各頂点のラベルのリストを返す
    return label, group


# 縮約後のグラフを構築
def construct(N, G, label, group):
    """
    縮約したノードのグラフを作る
    G0[i]: ラベルiと隣接するラベルのset
    GP[i]: ラベルiに含まれるノードのリスト
    """
    G0 = [set() for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
    return G0


N, M = [int(_) for _ in input().split()]
G = [[] for i in range(N)]
RG = [[] for i in range(N)]

for i in range(M):
    a, b = [int(_) for _ in input().split()]
    G[a - 1].append(b - 1)
    RG[b - 1].append(a - 1)

label, group = scc(N, G, RG)
del RG
G0 = construct(N, G, label, group)
del G


def dfs2(s):
    global G0
    used[s] = 1
    # 順方向の有向グラフ
    for t in G0[s]:
        if not used[t]:
            dfs2(t)
    return


ans = 0
used = [0] * label
for i in range(label):
    # dfsでたどれてないところがあればたどる（連結でないグラフ）
    if not used[i]:
        ans += 1
        dfs2(i)
print(ans)