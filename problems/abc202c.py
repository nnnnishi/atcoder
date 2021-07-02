from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

dicA = defaultdict(int)
dicB = defaultdict(int)

for i in range(N):
    dicA[A[i]] += 1
    dicB[C[i]] += 1
ans = 0
for i in range(N):
    ans += dicA[B[i]] * dicB[i + 1]

print(ans)
