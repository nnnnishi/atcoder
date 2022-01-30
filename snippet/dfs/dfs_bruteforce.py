# 一番最初のindexから貪欲につめる
# https://atcoder.jp/contests/abc236/tasks/abc236_d
import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline
N = int(input())
A = []
for i in range(2 * N - 1):
    A.append(list(map(int, input().split())))
ans = 0


def dfs(n, used, cnt):
    global ans
    if n == 2 * N:
        if ans < cnt:
            ans = cnt
        return
    else:
        for i in range(2 * N):
            if not used[i]:
                used[i] = True
                for j in range(i, 2 * N):
                    if not used[j]:
                        used[j] = True
                        dfs(n + 2, used, cnt ^ A[i][j - i - 1])
                        used[j] = False
                used[i] = False
                break
    return


dfs(0, [False] * (2 * N), 0)
print(ans)
