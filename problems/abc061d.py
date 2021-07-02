# O(EV)
def bellman_ford(ini, G, V):
    d = [-float("inf")] * V  # 各頂点への最小コスト
    d[ini] = 0  # 自身への距離は0
    for i in range(V):
        update = False  # 更新が行われたか
        # すべての辺をたどる
        for s, e, c in G:
            if d[e] < d[s] + c:
                d[e] = d[s] + c
                if e == V - 1:
                    update = True
        if not update:
            break
        # V-1回以上更新できる場合は負閉路が存在
        if i == V - 1:
            exit(print("inf"))
    return print(d[V - 1])


V, M = [int(_) for _ in input().split()]
G = []
for _ in range(M):
    s, e, c = [int(x) for x in input().split()]  # 始点,終点,コスト
    # 0はじまりにする
    s -= 1
    e -= 1
    G.append([s, e, c])

bellman_ford(0, G, V)
