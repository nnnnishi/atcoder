import sys

sys.setrecursionlimit(1000000)

# N: 頂点数
N = int(input())
# G[v]: 頂点vの子頂点 (親頂点は含まない)
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = [int(_) for _ in input().split()]
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

dp = [0] * N


def dfs(pos, pre):
    dp[pos] = 1
    for g in G[pos]:
        if g == pre:
            continue
        dp[pos] += dfs(g, pos)
    return dp[pos]


dfs(0, -1)
ans = 0
for i in range(N):
    ans += dp[i] * (N - dp[i])

print(ans)