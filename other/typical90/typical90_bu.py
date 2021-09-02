from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
c = input().split()

node = [[] for _ in range(N)]  # 隣接リスト
e = []
for i in range(N - 1):
    x, y = map(int, input().split())
    e.append((x - 1, y - 1))
    node[x - 1].append(y - 1)
    node[y - 1].append(x - 1)


mod = 10 ** 9 + 7
p = [-1] * N  # p[i] はi の親。根なら-1
q = deque([0])  # 根はどこでも良い
r = []
# トポロジカルソート
while q:
    i = deque.popleft(q)
    r.append(i)
    # print(node[i])
    for a in node[i]:  # i の子node を探索する
        if p[a] != -1:
            continue
        p[a] = i
        node[a].remove(i)  # 子への頂点のみを持つ
        deque.append(q, a)

dp = [[0, 0, 0] for _ in range(N)]

for i in range(N):
    if c[i] == "a":
        dp[i][0] = 1
    else:
        dp[i][1] = 1
# print(dp)
# print(node)
# print("*" * 10)
for p in r[::-1]:
    if dp[p][0] == 1:
        i1, i2 = 1, 1
        for i in node[p]:  # おやへ値を足していく
            # iについてきらないとき+きるとき
            dp[p][0] *= dp[i][0] + dp[i][2]
            dp[p][0] %= mod
            # dp[i][0]とdp[i][2]はあとから引く
            i1 *= dp[i][0] + dp[i][1] + 2 * dp[i][2]
            # iについてきらないとき
            i2 *= dp[i][0] + dp[i][2]
        dp[p][2] = i1 - i2
        dp[p][2] %= mod
    else:
        i1, i2 = 1, 1
        for i in node[p]:  # おやへ値を足していく
            # a
            dp[p][1] *= dp[i][1] + dp[i][2]
            dp[p][1] %= mod
            i1 *= dp[i][0] + dp[i][1] + 2 * dp[i][2]
            i2 *= dp[i][1] + dp[i][2]
        dp[p][2] = i1 - i2
        dp[p][2] %= mod

print(dp[p][2])