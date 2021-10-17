from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

S = list(input())
d = defaultdict(int)

for s in S:
    d[s] += 1
odd = []
even = []
for k, v in d.items():
    if v % 2 == 0:
        even.append(v)
    else:
        odd.append(v)

if len(odd) == 0:
    exit(print(len(S)))

res = len(S) - len(odd)
part = res // 2
mins = part // len(odd)
print(1 + mins * 2)

