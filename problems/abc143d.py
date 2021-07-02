from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import sys

N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        ans += bisect_left(L[j + 1 :], L[i] + L[j])
print(ans)
