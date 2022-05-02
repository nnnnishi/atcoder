# https://atcoder.jp/contests/typical90/tasks/typical90_bc
N, P, Q = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

ans = 0


def dfs(i, c, n):
    """
    5個の積をPで割ってQになるパターン数のdfs
    深さが5ばらpypy
    """
    global ans
    c %= P
    if n == 5:
        if c == Q:
            ans += 1
        return
    else:
        for j in range(i + 1, N):
            if A[j] == 0:
                dfs(j, 0, n + 1)
            else:
                c *= A[j]
                dfs(j, c, n + 1)
                c //= A[j]
    return


dfs(-1, 1, 0)
print(ans)
