from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
l = []
waza = set()
for i in range(N):
    l.append([int(_) for _ in input().split()])

q = deque()
ans = 0
waza.add(N - 1)
for i in l[N - 1][2:]:
    q.append(i - 1)
while len(q) > 0:
    e = q.popleft()
    waza.add(e)

    for i in l[e][2:]:
        if i - 1 not in waza:
            q.append(i - 1)

for w in waza:
    ans += l[w][0]
print(ans)
