from audioop import reverse
import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N, Q = [int(_) for _ in input().split()]
X = [int(_) for _ in input().split()]
dp = [[] for _ in range(N)]
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(_) for _ in input().split()]
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)
query = []
for _ in range(Q):
    query.append([int(_) for _ in input().split()])

# 深さ優先
def dfs(pos, pre):
    global dp
    dp[pos].append(X[pos])
    for i in G[pos]:
        if i != pre:
            dfs(i, pos)
            dp[i].sort(reverse=True)
            if len(dp[i]) > 20:
                dp[pos] += dp[i][:20]
            else:
                dp[pos] += dp[i]
    return


ans = 0
dfs(0, -1)
dp[0].sort(reverse=True)
for v, k in query:
    v -= 1
    print(dp[v][k - 1])

