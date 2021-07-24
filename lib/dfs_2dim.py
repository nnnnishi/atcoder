import sys

sys.setrecursionlimit(1000000)

# 深さ優先
def dfs(i):
    global ans
    y = i[0]
    x = i[1]
    if y == gy and x == gx:
        ans = True
    v[y][x] = False
    for y2, x2 in [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]:
        if 0 <= x2 < W and 0 <= y2 < H and v[y2][x2] == True:
            dfs([y2, x2])
