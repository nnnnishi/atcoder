from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = []
dic = defaultdict(int)
for i in range(N):
    a = int(input())
    if dic[a] == 0:
        dic[a] = 1
    else:
        dic[a] = 0
ans = 0
for x in dic:
    ans += dic[x]
print(ans)
