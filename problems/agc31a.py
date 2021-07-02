from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
S = input()
c = Counter(list(S))
MOD = 10 ** 9 + 7
ans = 1
for i in c.values():
    ans = ans * (i + 1) % MOD
print(ans - 1)
