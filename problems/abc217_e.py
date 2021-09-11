from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations


Q = int(input())
q = deque()
h = []
hn = 0
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        q.append(query[1])
    elif query[0] == 3:
        # ソートする、ソート済みの数hnを更新
        for qi in q:
            heappush(h, qi)
        q = deque()
        hn = len(h)
    else:
        # ソート済みの数
        if hn > 0:
            e = heappop(h)
            # print("*", e)
            print(e)
            hn -= 1
        else:
            e = q.popleft()
            print(e)
