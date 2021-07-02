from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = list(map(int, input().split()))
G = [[] for i in range(N)]

for i in range(M):
    A, B = list(map(int, input().split()))
    G[A - 1].append(B - 1)


def check(n):
    q = deque()
    q.append(n)
    goSet = set()
    goSet.add(n)
    while len(q) > 0:
        i = q.popleft()
        for j in G[i]:
            if j not in goSet:
                goSet.add(j)
                q.append(j)
    return len(goSet)


ans = 0
for z in range(N):
    ans += check(z)
print(ans)