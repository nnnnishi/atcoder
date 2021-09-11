from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
a = [int(_) for _ in input().split()]

d = defaultdict(int)
for i in range(N):
    d[a[i]] += 1

l = []

for k in d.keys():
    if d[k] % 2 == 0:
        l.append([k, 2])
    else:
        l.append([k, 1])
q = deque()

l.sort()

for li in l:
    q.append(li)

ans = len(l)
while len(q) > 0:
    mi = q.popleft()
    while mi[1] == 1:
        if len(q) > 0:
            mi = q.popleft()
        else:
            break
    if len(q) > 0:
        ma = q.pop()
        while ma[1] == 1:
            if len(q) > 0:
                ma = q.pop()
            else:
                ans -= 1
                break
    else:
        if mi[1] == 2:
            ans -= 1

print(ans)