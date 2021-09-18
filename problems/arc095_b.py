from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
a = [int(_) for _ in input().split()]

# Nが大きい
def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result


a.sort()
maxa = a[-1]
if len(a) == 2:
    exit(print(a[1], a[0]))
mid = maxa // 2
i = bisect_right(a, mid)
if i - 1 >= 0:
    if abs(mid - a[i - 1]) < abs(mid - a[i]):
        print(maxa, a[i - 1])
    else:
        print(maxa, a[i])
else:
    print(maxa, a[i])
