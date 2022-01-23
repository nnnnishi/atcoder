import sys
from itertools import accumulate, product, permutations, combinations

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


a, N = [int(_) for _ in input().split()]

visited = set()
ans = []
# 深さ優先
def dfs(x, cnt):
    global ans
    if x == N:
        ans.append(cnt)
    else:
        if x in visited or x >= 10 ** 6 + 1:
            return
        else:
            visited.add(x)
            dfs(a * x, cnt + 1)
            if x >= 10:
                for _ in range(len(str(x))):
                    if x % 10 != 0:
                        cnt += 1
                        x = int(str(x)[-1] + str(x)[:-1])
                        dfs(x, cnt)
                    else:
                        break
            return


dfs(1, 0)
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
