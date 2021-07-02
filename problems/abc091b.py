from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

dic = defaultdict(int)
N = int(input())
for i in range(N):
    dic[input()] += 1

M = int(input())
for i in range(M):
    dic[input()] -= 1
ans = 0
for x in dic:
    if dic[x] > 0:
        ans = max(ans, dic[x])
print(ans)