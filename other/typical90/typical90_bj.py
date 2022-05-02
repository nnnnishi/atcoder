from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
S = [set() for _ in range(N)]
d = defaultdict(list)
for i in range(N):
    a, b = [int(_) for _ in input().split()]
    S[i].add(a - 1)
    S[i].add(b - 1)
    d[a - 1].append(i)
    d[b - 1].append(i)
# print(S)
q = deque()
ans = []
anss = set()
# まずさいごにいれられる候補を詰める
for i in range(N):
    if i in S[i]:
        ans.append(i + 1)
        anss.add(i)
        q.append(i)

while len(ans) < N:
    if len(q) == 0:
        print(-1)
        exit()
    else:
        i = q.pop()
        for j in d[i]:
            if j not in anss:
                ans.append(j + 1)
                anss.add(j)
                q.append(j)

print(*ans[::-1])
