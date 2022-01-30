# https://algo-logic.info/tree-diameter/
import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N = int(input())
dp = [0] * N
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(_) for _ in input().split()]
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)


visited = set()

# 深さ優先
def dfs(pos, cnt):
    global dp
    visited.add(pos)
    for i in G[pos]:
        if i not in visited:
            dp[i] = cnt + 1
            dfs(i, cnt + 1)
    return


dfs(0, 0)
max_depth = 0
idx = -1
for i in range(N):
    if dp[i] > max_depth:
        max_depth = dp[i]
        idx = i

dp = [0] * N
visited = set()
dfs(idx, 0)
for i in range(N):
    if dp[i] > max_depth:
        max_depth = dp[i]

print(max_depth + 1)
