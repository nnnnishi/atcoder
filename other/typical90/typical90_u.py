# 強連結成分分解(Strongly Connected Components: SCC): グラフGに対するSCCを行う
import sys

sys.setrecursionlimit(1000000)
# Nが大きい
def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result


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
    GP = [[] for i in range(label)]
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
G = [[] for i in range(N)]
RG = [[] for i in range(N)]

for i in range(M):
    a, b = [int(_) for _ in input().split()]
    G[a - 1].append(b - 1)
    RG[b - 1].append(a - 1)

label, group = scc(N, G, RG)
G0, GP = construct(N, G, label, group)
# print(GP)
ans = 0
for i in range(label):
    if len(GP[i]) >= 2:
        ans += cmb(len(GP[i]), 2)
print(ans)