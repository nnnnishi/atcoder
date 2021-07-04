import sys

sys.setrecursionlimit(1000000)
n, m, q = [int(_) for _ in input().split()]
Q = []
for i in range(q):
    a, b, c, d = [int(_) for _ in input().split()]
    Q.append([d, b - 1, a - 1, c])

ans = 0


def dfs(L):
    global ans
    if len(L) == n:
        tmp = 0
        for d, b, a, c in Q:
            if L[b] - L[a] == c:
                tmp += d
        ans = max(ans, tmp)
        return
    else:
        for i in range(L[-1], m + 1):
            dfs(L + [i])
    return


for i in range(1, m + 1):
    dfs([i])
print(ans)