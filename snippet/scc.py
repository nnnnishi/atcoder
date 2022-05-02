# 強連結成分分解(Strongly Connected Components: SCC): グラフGに対するSCCを行う
# https://manabitimes.jp/math/1250
# https://tjkendev.github.io/procon-library/python/graph/scc.html
# https://atcoder.jp/contests/typical90/tasks/typical90_u
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/021.jpg

import sys

input = sys.stdin.readline
# 小さいとRE
# dfsベースなので長いとpypyよりpythonのほうがはやい
sys.setrecursionlimit(1000000)


def scc(N, G, RG):
    """
    入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
    出力: (n_label: <ラベル数>, group <各頂点のラベル番号のリスト>)
    """
    order = []
    group = [None] * N

    def dfs(s):
        used[s] = 1
        # 順方向の有向グラフ
        for t in G[s]:
            if not used[t]:
                dfs(t)
        # でてきたときにsを足す（帰りがけ順）
        order.append(s)

    def rdfs(s, n_label):
        group[s] = n_label
        used[s] = 1
        # 逆方向の有向グラフ
        for t in RG[s]:
            if not used[t]:
                rdfs(t, n_label)

    used = [0] * N
    for i in range(N):
        # dfsでたどれてないところがあればたどる（連結でないグラフ）
        if not used[i]:
            dfs(i)

    used = [0] * N
    n_label = 0
    # 帰りがけ順の逆からたどる
    for s in reversed(order):
        if not used[s]:
            # rdfsで0からラベル付けする
            rdfs(s, n_label)
            n_label += 1
    # ラベルと各頂点のラベルのリストを返す
    return n_label, group


# 縮約後のグラフを構築
def construct(N, G, n_label, group):
    """
    縮約したノードのグラフを作る
    G0[i]: ラベルiと隣接するラベルのset
    GP[i]: ラベルiに含まれるノードのリスト
    """
    G0 = [set() for _ in range(n_label)]
    GP = [[] for _ in range(n_label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP


N, M = [int(_) for _ in input().split()]
G = [[] for _ in range(N)]
RG = [[] for _ in range(N)]

for _ in range(M):
    a, b = [int(_) for _ in input().split()]
    G[a - 1].append(b - 1)
    RG[b - 1].append(a - 1)

# n_label: ラベル数, group: 各頂点のラベル番号のリスト)
n_label, group = scc(N, G, RG)

# G0: n_labelと隣接するn_labelの集合, GP: n_labelに含まれる点のリスト
# G0はトポロジカルソートされている
G0, GP = construct(N, G, n_label, group)
print(G0)
print(GP)
# この問題ではG0はつかわず、GP(あるラベルに含まれる点のリスト)だけつかう
ans = 0
for i in range(n_label):
    if len(GP[i]) >= 2:
        # len(GP[i])から2つえらぶ
        ans += len(GP[i]) * (len(GP[i]) - 1) // 2
print(ans)
