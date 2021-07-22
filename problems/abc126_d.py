# 再帰用
import sys

sys.setrecursionlimit(1000000)

N = int(input())
color = [-1] * N
G = [[] for _ in range(N)]
W = {}
for i in range(N - 1):
    u, v, w = [int(_) for _ in input().split()]
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)
    W.setdefault(u - 1, {})
    W[u - 1][v - 1] = w
    W.setdefault(v - 1, {})
    W[v - 1][u - 1] = w


def dfs(vi, c):
    for vj in G[vi]:
        if color[vj] == -1:
            if W[vi][vj] % 2 == 0:
                color[vj] = c
            else:
                color[vj] = (c + 1) % 2
            dfs(vj, color[vj])
    return


color[0] = 0
dfs(0, 0)
for a in color:
    print(a)
