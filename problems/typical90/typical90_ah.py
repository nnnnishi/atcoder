from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, K = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
q = deque()
d = defaultdict(int)
c = 0
ans = 0
tmp = 0
for i in range(N):
    q.append(a[i])
    if d[a[i]] == 0:
        c += 1
        tmp += 1
        d[a[i]] += 1
        while c > K:
            j = q.popleft()
            d[j] -= 1
            tmp -= 1
            if d[j] == 0:
                c -= 1
    else:
        d[a[i]] += 1
        tmp += 1
    ans = max(ans, tmp)
print(ans)