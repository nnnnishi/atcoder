N = int(input())
K = int(input())

from functools import lru_cache


@lru_cache(maxsize=None)
def dfs(n, k):
    strN = str(n)
    lenN = len(list(strN))
    if lenN < k:
        return 0
    if k == 0:
        return 1
    if lenN == 1:
        return n
    # nの下一桁が0
    if strN[lenN - 1] == "0":
        return (
            dfs(int(strN[0 : lenN - 1]), k)
            + dfs(int(strN[0 : lenN - 1]) - 1, k - 1) * 9
        )
    else:
        # nの下一桁が0以外
        return (
            dfs(int(strN[0 : lenN - 1]), k - 1) * int(strN[lenN - 1])
            + dfs(int(strN[0 : lenN - 1]) - 1, k - 1) * (9 - int(strN[lenN - 1]))
            + dfs(int(strN[0 : lenN - 1]), k)
        )


print(dfs(N, K))
