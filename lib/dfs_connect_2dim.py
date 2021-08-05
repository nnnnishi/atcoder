import sys
from itertools import accumulate, product, permutations, combinations

sys.setrecursionlimit(1000000)


N = 10
S = [list(input()) for i in range(N)]
k = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            k += 1
if k == 100:
    exit("YES")
visited = set()


# 深さ優先
def dfs(y, x):
    # すでにパターンを確認済みであれば探索しない
    if (y, x) in visited:
        return
    visited.add((y, x))
    # K個はいっていれば足す
    if len(visited) == k + 1:
        exit(print("YES"))
    else:
        # 次行く場所を全探索
        for ny, nx in [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]:
            if 0 <= ny < N and 0 <= nx < N and S[ny][nx] == "o":
                dfs(ny, nx)
        return


for sy in range(N):
    for sx in range(N):
        visited = set()
        if S[sy][sx] == "x":
            dfs(sy, sx)

print("NO")
