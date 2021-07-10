from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import string


N = int(input())
c = Counter(list(input()))
for i in range(N - 1):
    c2 = Counter(list(input()))
    for k in c:
        if c2[k] <= c[k]:
            c[k] = c2[k]
ans = ""
for s in list(string.ascii_lowercase):
    ans += s * c[s]
print(ans)
