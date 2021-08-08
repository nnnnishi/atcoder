# O(V+E) 頂点と辺を順に見る
import sys

sys.setrecursionlimit(1000000)


N, M = [int(_) for _ in input().split()]
# 無色は-1, {0,1}でいろつける
color = [-1] * N
G = [[] for _ in range(N)]
# 木だったらMでなくN-1
for i in range(M):
    a, b = [int(_) for _ in input().split()]
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def dfs(vi, c):
    color[vi] = c
    for vj in G[vi]:
        # 隣接が同じ色はだめ
        if color[vj] == c:
            return False
        else:
            # 色がついていない場合は違う色でぬれなかったらだめ
            if color[vj] == -1 and not dfs(vj, (c + 1) % 2):
                return False
    return True


# 連結ならばチェックは一回、連結でなければすべての未着色の頂点から試す
# 2部グラフならKを片方のいろの要素数としてK*(N-K)
if dfs(0, 0):
    K = sum(color)
    print(K * (N - K) - M)
# 2部グラフでなければ全部つなぐ
else:
    print(N * (N - 1) // 2 - M)
