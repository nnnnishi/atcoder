# O(log(N))で追加取り出し, heapfyはnlogn
# https://atcoder.jp/contests/code-thanks-festival-2017-open/tasks/code_thanks_festival_2017_c
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge

N, K = [int(_) for _ in input().split()]
l = []
for i in range(N):
    a, b = [int(_) for _ in input().split()]
    l.append([a, b])
# 最初に順序をつけておく
heapify(l)
c = 0
t = 0
for _ in range(K):
    # 取り出す
    a, b = heappop(l)
    t += a
    c += 1
    # 追加する
    heappush(l, [a + b, b])
print(t)
