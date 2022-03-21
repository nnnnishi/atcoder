import sys

sys.setrecursionlimit(1000000)

N, X = list(map(int, input().split()))
A = []
Ls = []
for _ in range(N):
    L, *a = [int(_) for _ in input().split()]
    A.append(a)
    Ls.append(L)

ans = 0


def dfs(i, mul):
    global ans
    if i == N:
        if mul == X:
            ans += 1
        return
    else:
        if mul <= X:
            for j in range(Ls[i]):
                dfs(i + 1, mul * A[i][j])
        return


dfs(0, 1)
print(ans)
