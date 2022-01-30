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

# 深さ優先
visited = set()


def dfs(pos, pre, cnt):
    global dp
    for i in G[pos]:
        if i not in visited and i != pre:
            dp[i] = cnt + 1
            visited.add(i)
            dfs(i, pos, cnt + 1)
    return


visited.add(0)
dfs(0, -1, 0)
max_depth = 0
idx = -1
for i in range(N):
    if dp[i] > max_depth:
        max_depth = dp[i]
        idx = i

dp = [0] * N
visited = set()
dfs(idx, -1, 0)
for i in range(N):
    if dp[i] > max_depth:
        max_depth = dp[i]
        idx = i

print(max_depth + 1)
