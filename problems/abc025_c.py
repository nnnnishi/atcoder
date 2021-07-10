# 再帰用
import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)

b = [[int(_) for _ in input().split()] for i in range(2)]
c = [[int(_) for _ in input().split()] for i in range(3)]
tot = 0
for i in range(2):
    tot += sum(b[i])
for i in range(3):
    tot += sum(c[i])
init = [["0"] * 3 for i in range(3)]


def score(st):
    # b
    dai = 0
    for x in range(3):
        for y in range(2):
            if st[x][y] == st[x][y + 1]:
                dai += b[y][x]
    for x in range(2):
        for y in range(3):
            if st[x][y] == st[x + 1][y]:
                dai += c[y][x]
    return dai


def dfs(st, num):
    if num == 9:
        tmp = score(st)
        return tmp
    else:
        if num % 2 == 0:
            # chokudai
            ret = -(10 ** 10)
            for y in range(3):
                for x in range(3):
                    if st[y][x] == "0":
                        st[y][x] = "o"
                        ret = max(ret, dfs(st, num + 1))
                        st[y][x] = "0"
        else:
            # naoko
            ret = 10 ** 10
            for y in range(3):
                for x in range(3):
                    if st[y][x] == "0":
                        st[y][x] = "x"
                        ret = min(ret, dfs(st, num + 1))
                        st[y][x] = "0"
        return ret


dai = dfs(init, 0)
print(dai)
print(tot - dai)
