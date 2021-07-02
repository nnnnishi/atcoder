import sys

sys.setrecursionlimit(1000000)
m = int(input())
n = int(input())
A = [[int(_) for _ in input().split()] for i in range(n)]

ans = 0


def dfs(y1, x1, cnt):
    global ans
    ans = max(ans, cnt)
    # print(x1, y1, cnt, ans)
    # みぎ、ひだり、うえ、した
    for y2, x2 in [(y1, x1 + 1), (y1, x1 - 1), (y1 + 1, x1), (y1 - 1, x1)]:
        if 0 <= y2 <= n - 1 and 0 <= x2 <= m - 1 and A[y2][x2] == 1:
            A[y2][x2] = 0
            dfs(y2, x2, cnt + 1)
            A[y2][x2] = 1
    return


for y in range(n):
    for x in range(m):
        check = 0
        if A[y][x] == 1:
            for y2, x2 in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:
                if 0 <= y2 <= n - 1 and 0 <= x2 <= m - 1 and A[y2][x2] == 1:
                    check += 1
            if check <= 2:
                A[y][x] = 0
                dfs(y, x, 1)
                A[y][x] = 1
print(ans)