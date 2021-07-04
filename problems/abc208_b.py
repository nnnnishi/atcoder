import math


P = int(input())

ans = 0


def dfs(i, res):
    global ans
    if res % math.factorial(i) == 0:
        ans += res // math.factorial(i)
        exit(print(ans))
    else:
        ans += res // math.factorial(i)
        res = res - (res // math.factorial(i)) * math.factorial(i)
        dfs(i - 1, res)


dfs(10, P)
