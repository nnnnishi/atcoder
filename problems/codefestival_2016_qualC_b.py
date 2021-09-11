from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

K, T = [int(_) for _ in input().split()]
a = [-int(_) for _ in input().split()]
q = []
if len(a) > 1:
    for i in range(T):
        heappush(q, (a[i], i))
else:
    exit(print(-a[0] - 1))

n, e1 = heappop(q)
b = e1
heappush(q, (n + 1, b))
ans = 0
while n < 0:
    n1, e1 = heappop(q)
    n2, e2 = heappop(q)
    if e1 != b:
        b = e1
        heappush(q, (n1 + 1, b))
        heappush(q, (n2, e2))
        n = min(n1 + 1, n2)
    else:
        if n2 < 0:
            b = e2
            heappush(q, (n2 + 1, b))
            heappush(q, (n1, e1))
            n = min(n2 + 1, n1)
        else:
            b = e1
            heappush(q, (n1 + 1, b))
            heappush(q, (n2, e2))
            n = min(n1 + 1, n2)
            ans += 1
print(ans)
