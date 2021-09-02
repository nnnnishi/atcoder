from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

# Bit全探索
# N桁の数のうちM桁に1がたつものの数を数える
Y, X = [int(_) for _ in input().split()]
P = [[int(_) for _ in input().split()] for i in range(Y)]


def has_bit(n, i):
    return (n & 1 << i) > 0


ans = 0
# N桁の0-1の組合せパターン数 1<<N
for n in range(1, 1 << Y):
    cnt = 0
    y_list = []
    for i in range(Y):
        # パターンnのi桁目が1(つかう)
        if has_bit(n, i):
            y_list.append(i)
    a_list = []
    for x in range(X):
        tset = set()
        for y in y_list:
            tset.add(P[y][x])
        if len(tset) == 1:
            a_list.append(tset.pop())
    c = Counter(a_list)
    # print(y_list)
    # print(c)
    if len(c) > 0:
        ans = max(c.most_common()[0][1] * len(y_list), ans)
print(ans)