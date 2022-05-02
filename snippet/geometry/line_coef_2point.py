from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations


def calc_coef(p1, p2):
    # p1=(x1,y1), p2=(x2,y2)の2点を通る直線の方程式の係数abcを求める
    # ax+by+c=0
    x1, y1 = p1
    x2, y2 = p2
    a = y2 - y1
    b = x1 - x2
    c = y1 * x2 - x1 * y2
    return (a, b, c)


N, K = [int(_) for _ in input().split()]
point = []
for _ in range(N):
    x, y = [int(_) for _ in input().split()]
    point.append((x, y))
if K == 1:
    print("Infinity")
    exit()
elif K > N:
    print(0)
    exit()
coef_s = set()
for c in combinations(point, 2):
    p1, p2 = c
    t = calc_coef(p1, p2)
    coef_s.add(t)

ans_s = set()
for a, b, c in coef_s:
    cand = set()
    for x, y in point:
        if a * x + b * y + c == 0:
            cand.add((x, y))
    if len(cand) >= K:
        ans_s.add(tuple(cand))
# print(ans_s)
print(len(ans_s))
