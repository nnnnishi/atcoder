import sys
from itertools import accumulate, product, permutations, combinations

sys.setrecursionlimit(1000000)


N, M = [int(_) for _ in input().split()]
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = [int(_) for _ in input().split()]
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

# 深さ優先
def dfs(i, j):
    cnt = 0
    # すでにパターンを確認済みであれば探索しない
    if j in visited:
        return 1
    visited.add(j)
    # 次行く場所を全探索
    for k in G[j]:
        if k != i:
            cnt += dfs(j, k)
    return cnt


visited = set()
ans = 0
for s in range(N):
    if s not in visited:
        if dfs(-1, s) == 0:
            ans += 1

print(ans)