from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

K = int(input())
S = list(input())
T = list(input())
# 全パターン
all = (9 * K - 8) * (9 * K - 9)
ac = Counter(list(map(int, T[:4] + S[:4])))
cnt = 0
for s in range(1, 10):
    for t in range(1, 10):
        sc = Counter(list(map(int, S[:4])) + [s])
        tc = Counter(list(map(int, T[:4])) + [t])
        s_cnt = 0
        for k in range(1, 10):
            s_cnt += k * (10 ** sc[k])
        t_cnt = 0
        for k in range(1, 10):
            t_cnt += k * (10 ** tc[k])
        if s_cnt > t_cnt:
            if s == t:
                if K - ac[s] >= 2:
                    cnt += (K - ac[s]) * (K - ac[s] - 1)
            else:
                if K - ac[s] >= 1 and K - ac[t] >= 1:
                    cnt += (K - ac[s]) * (K - ac[t])
print(cnt / all)
