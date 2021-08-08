import sys
from itertools import accumulate, product, permutations, combinations

sys.setrecursionlimit(1000000)


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(_) for _ in input().split()]
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

for i in range(N):
    G[i].sort()

# 深さ優先
def dfs(i):
    global ans
    ans.append(i + 1)
    visited.add(i)
    # 次行く場所を全探索
    for j in G[i]:
        if j not in visited:
            dfs(j)
            ans.append(i + 1)
    return


visited = set()
ans = []
dfs(0)

print(*ans)