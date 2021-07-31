from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

S = list(input())
c = Counter(S)

if len(S) <= 1:
    st = 1
    en = 10
elif len(S) <= 2:
    st = 10
    en = 100
else:
    st = 100
    en = 1000

for i in range(st, en):
    if i % 8 == 0:
        d = Counter(str(i))
        for k in d.keys():
            if c[k] < d[k]:
                break
        else:
            exit(print("Yes"))
print("No")
