import sys
from itertools import accumulate, product, permutations, combinations

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = [int(_) for _ in input().split()]
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

# 深さ優先
def dfs(s, c):
    # すでにパターンを確認済みであれば探索しない
    if s not in visited:
        visited.add(s)
        color[s] = c
        # 次行く場所を全探索
        for t in G[s]:
            dfs(t, (c + 1) % 2)
        return


color = [None] * N
visited = set()
ans = 0
dfs(0, 0)

check = 0
if sum(color) >= N // 2:
    check = 1
cnt = 0
for i in range(N):
    if color[i] == check:
        print(i + 1)
        cnt += 1
        if cnt == N // 2:
            exit()
