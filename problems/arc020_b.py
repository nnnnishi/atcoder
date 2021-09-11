from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

n, c = [int(_) for _ in input().split()]
e = defaultdict(int)
o = defaultdict(int)
for i in range(n):
    a = int(input())
    if i % 2 == 0:
        e[a] += 1
    else:
        o[a] += 1

on = n // 2
if n % 2 == 0:
    en = n // 2
else:
    en = n // 2 + 1

even = []
odd = []

for k in e.keys():
    even.append((e[k], k))
for k in o.keys():
    odd.append((o[k], k))
even.sort(reverse=True)
odd.sort(reverse=True)

if even[0][1] != odd[0][1]:
    print((en - even[0][0] + on - odd[0][0]) * c)
else:
    if len(even) > 1 and len(odd) > 1:
        print(
            (min(en - even[0][0] + on - odd[1][0], en - even[1][0] + on - odd[0][0]))
            * c
        )
    elif len(even) > 1:
        print((min(en - even[0][0] + on, en - even[1][0])) * c)
    elif len(odd) > 1:
        print((min(on - odd[1][0], en + on - odd[0][0])) * c)
    else:
        print((min(on, en)) * c)
