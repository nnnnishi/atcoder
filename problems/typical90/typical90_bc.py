# 再帰用
import sys

sys.setrecursionlimit(1000000)

N, P, Q = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
for i in range(N):
    A[i] %= P
ans = 0


def dfs(i, c, prd):
    global ans
    if c >= 5:
        if prd % P == Q:
            ans += 1
        return
    else:
        if i < N - 1 and N - 1 - i >= 5 - c:
            dfs(i + 1, c + 1, prd * A[i + 1] % P)
            dfs(i + 1, c, prd)
    return


dfs(-1, 0, 1)
print(ans)
