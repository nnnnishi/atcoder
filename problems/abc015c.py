# 再帰用
import sys

sys.setrecursionlimit(1000000)

N, K = [int(_) for _ in input().split()]

T = []
for k in range(N):
    T.append([int(_) for _ in input().split()])


def dfs(d, check):
    if d == N:
        if check == 0:
            exit(print("Found"))
    else:
        # 各選択肢を代入
        for k in range(K):
            dfs(d + 1, (check ^ T[d][k]))
        return


for k in range(K):
    dfs(1, T[0][k])
print("Nothing")
