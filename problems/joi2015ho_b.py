import sys

sys.setrecursionlimit(10 ** 9)
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

dp = [[0] * N for _ in range(N)]
# dp[i][j] = 区間[i,j]が残っている時のJOIくんの取り分の最大値(反時計回り)


def dfs(i, j, picked):
    # メモ
    if dp[i][j] > 0:
        return dp[i][j]
    if i == j:
        if picked % 2 == 0:
            dp[i][j] = A[i]
            return A[i]
        else:
            return 0

    di = (i + 1) % N
    dj = j - 1 if j - 1 >= 0 else N - 1

    if picked % 2 == 0:  # JOIくんの番
        ret = max(dfs(di, j, picked + 1) + A[i], dfs(i, dj, picked + 1) + A[j])
    else:  # IOIちゃんの番
        if A[i] > A[j]:
            ret = dfs(di, j, picked + 1)
        else:
            ret = dfs(i, dj, picked + 1)

    dp[i][j] = ret
    return ret


ans = 0
for i in range(N):
    start = (i + 1) % N
    end = i - 1 if i - 1 >= 0 else N - 1
    r = dfs(start, end, 1) + A[i]
    ans = max(ans, r)

print(ans)