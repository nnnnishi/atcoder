from collections import deque, defaultdict
import sys

input = sys.stdin.readline
# 小さいとRE
# dfsベースなのでpypyよりpythonのほうが早いこともある
sys.setrecursionlimit(1000000)
N, M, K = map(int, input().split())
ab = []
for _ in range(M):
    ab.append(tuple(map(int, input().split())))

in_cnt = [0] * (N + 1)
outs = [[] for _ in range(N + 1)]
for a, b in ab:
    # 入次数
    in_cnt[b - 1] += 1
    # 出先のノード
    outs[a - 1].append(b - 1)

ans = []
res = []
# 入次数が0のノードのqueue
q = deque([i for i in range(N) if in_cnt[i] == 0])


def dfs(n):
    # global ans
    # global in_cnt
    # global outs
    # print(res)
    if n == N:
        ans.append(res[:])
        if len(ans) == K:
            for i in range(K):
                print(*ans[i])
            exit()
        else:
            return
    else:
        if len(q) == 0:
            print(-1)
            exit()
        for i in range(min(len(q), K)):
            v = q.popleft()
            res.append(v + 1)
            sub_v = []
            for v2 in outs[v]:
                in_cnt[v2] -= 1
                sub_v.append(v2)
                if in_cnt[v2] == 0:
                    q.append(v2)
            dfs(n + 1)
            res.pop()
            for v2 in sub_v:
                in_cnt[v2] += 1
                if in_cnt[v2] == 1:
                    q.pop()
            q.append(v)
        return


dfs(0)
print(-1)
