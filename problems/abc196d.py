# 再帰用
import sys

sys.setrecursionlimit(1000000)

H, W, A, B = [int(_) for _ in input().split()]
used = []
for i in range(H):
    used.append([False] * W)
count = 0
ans = 0


def dfs(y, x):
    global count
    global ans
    if y == H - 1 and x == W - 1:
        if count == A:
            ans += 1
            return
    elif x == W - 1:
        # 縦置き
        if not (used[y][x] or used[y + 1][x]):
            count += 1
            used[y][x] = used[y + 1][x] = True
            dfs(y + 1, 0)
            used[y][x] = used[y + 1][x] = False
            count -= 1
        # 置かない
        dfs(y + 1, 0)
    elif y == H - 1:
        # 横置き
        if not (used[y][x] or used[y][x + 1]):
            count += 1
            used[y][x] = used[y][x + 1] = True
            dfs(y, x + 1)
            used[y][x] = used[y][x + 1] = False
            count -= 1
        # 置かない
        dfs(y, x + 1)
    else:
        # 横置き
        if not (used[y][x] or used[y][x + 1]):
            count += 1
            used[y][x] = used[y][x + 1] = True
            dfs(y, x + 1)
            used[y][x] = used[y][x + 1] = False
            count -= 1
        # 縦置き
        if not (used[y][x] or used[y + 1][x]):
            count += 1
            used[y][x] = used[y + 1][x] = True
            dfs(y, x + 1)
            used[y][x] = used[y + 1][x] = False
            count -= 1
        # 置かない
        dfs(y, x + 1)


dfs(0, 0)
print(ans)
