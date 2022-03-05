import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N = int(input())
dp = [[] for _ in range(N)]
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(_) for _ in input().split()]
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

# 深さ優先
cnt = 0


def dfs(pos, pre):
    global dp
    global cnt
    for i in G[pos]:
        if i != pre:
            dfs(i, pos)
            dp[pos] += [max(dp[i])]
            dp[pos] += [min(dp[i])]

    if len(dp[pos]) == 0:
        cnt += 1
        dp[pos] += [cnt]
    return


ans = 0
dfs(0, -1)
for i in range(N):
    if len(dp[i]) == 1:
        print(dp[i][0], dp[i][0])
    else:
        dp[i].sort()
        print(dp[i][0], dp[i][-1])

