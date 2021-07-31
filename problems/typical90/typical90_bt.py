# dfs_2dim_backtrack
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/072.jpg

import sys
from itertools import accumulate, product, permutations, combinations

Y, X = [int(_) for _ in input().split()]
A = [list(input()) for i in range(Y)]

sys.setrecursionlimit(1000000)


# 深さ優先
def dfs(y, x, c):
    # K個はいっていれば足す
    if c != 2 and A[y][x] == "G":
        global ans
        ans = max(c, ans)
        return
    else:
        # 次行く場所を全探索
        for y2, x2 in [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]:
            if 0 <= x2 < X and 0 <= y2 < Y and A[y2][x2] != "#":
                if (y2, x2) not in visited:
                    visited.add((y2, x2))
                    dfs(y2, x2, c + 1)
                    visited.remove((y2, x2))
    return


ans = 0
for y in range(Y):
    for x in range(X):
        if A[y][x] == ".":
            A[y][x] = "G"
            check = 0
            for y2, x2 in [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]:
                if 0 <= x2 < X and 0 <= y2 < Y and A[y2][x2] != "#":
                    check += 1
            if check >= 2:
                for y2, x2 in [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]:
                    if 0 <= x2 < X and 0 <= y2 < Y and A[y2][x2] != "#":
                        visited = set()
                        visited.add((y2, x2))
                        dfs(y2, x2, 1)
            A[y][x] = "#"
if ans == 0:
    print(-1)
else:
    print(ans)
