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
def dfs(pos, pre):
    global dp
    dp[pos] = 1
    for i in G[pos]:
        if i != pre:
            dfs(i, pos)
            dp[pos] += dp[i]
    return


ans = 0
dfs(0, -1)
for i in range(N):
    ans += dp[i] * (N - dp[i])
print(ans)
