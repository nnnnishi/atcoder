# https://atcoder.jp/contests/dp/tasks/dp_p
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/073.jpg

from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())

node = [[] for _ in range(N)]  # 隣接リスト
for i in range(N - 1):
    x, y = map(int, input().split())
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
# dp[i][0] = black, dp[i][1] = white
dp = [[1, 1] for _ in range(N)]

# print("*" * 10)
for p in r[::-1]:
    for i in node[p]:
        # おやがくろ、こは白
        dp[p][0] *= dp[i][1]
        dp[p][0] %= mod
        # おやがしろ、こはどちらでもOK
        dp[p][1] *= dp[i][0] + dp[i][1]
        dp[p][1] %= mod
print((dp[p][0] + dp[p][1]) % mod)
