# 枝の塗り分け
import sys

sys.setrecursionlimit(1000000)
from collections import defaultdict

N = int(input())
graph = [[] for _ in range(N)]
n2cs = [set() for _ in range(N)]
e2no = {}
colors = [-1] * (N - 1)
for i in range(N - 1):
    Ai, Bi = list(map(int, input().split()))
    graph[Ai - 1].append(Bi - 1)
    graph[Bi - 1].append(Ai - 1)
    e2no[(Ai - 1, Bi - 1)] = i


# 深さ優先
def dfs(i):
    visited.add(i)
    # 次行く場所を全探索
    for j in graph[i]:
        if j not in visited:
            for nc in range(c_start[i], N):
                if nc not in n2cs[i]:
                    if i < j:
                        colors[e2no[(i, j)]] = nc
                        c_start[i] = nc + 1
                    else:
                        colors[e2no[(j, i)]] = nc
                        c_start[i] = nc + 1
                    n2cs[j].add(nc)
                    n2cs[i].add(nc)
                    break
            dfs(j)
    return


visited = set()
c_start = defaultdict(int)
dfs(0)
print(max(colors) + 1)
for i in range(N - 1):
    print(colors[i] + 1)
