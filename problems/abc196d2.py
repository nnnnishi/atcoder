# 再帰用
import sys

sys.setrecursionlimit(1000000)

H, W, A, B = [int(_) for _ in input().split()]
used = []
for i in range(H):
    used.append([False] * W)


def dfs(x, y, a):
    # 最後までいってa==Aなら1を返しておわる、違ったら0を返して終わる
    if y == H:
        return a == 0
    if x == W:
        return dfs(0, y + 1, a)
    if used[y][x]:
        return dfs(x + 1, y, a)
    res = 0
    # 縦置き
    if y + 1 < H and not used[y + 1][x] and 0 < a:
        used[y][x] = used[y + 1][x] = True
        res += dfs(x + 1, y, a - 1)
        used[y][x] = used[y + 1][x] = False
    # 横置き
    if x + 1 < W and not used[y][x + 1] and 0 < a:
        used[y][x] = used[y][x + 1] = True
        res += dfs(x + 1, y, a - 1)
        used[y][x] = used[y][x + 1] = False
    # おかない
    res += dfs(x + 1, y, a)
    return res


print(dfs(0, 0, A))
