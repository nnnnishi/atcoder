from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [int(_) for _ in input().split()]
c = Counter(A)
Q = int(input())
setA = set(A)
sumA = sum(A)
for q in range(Q):
    B, C = [int(_) for _ in input().split()]
    if B in setA:
        sumA += (C - B) * c[B]
        c[C] += c[B]
        c[B] = 0
        setA.add(C)
    print(sumA)
