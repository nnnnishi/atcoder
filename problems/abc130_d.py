from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, K = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
sa = [0]
for i in range(len(a)):
    sa.append(sa[i] + a[i])
ans = 0
for i in range(len(sa)):
    c = K + sa[i]
    j = bisect_left(sa, c)
    ans += N - j + 1

print(ans)
