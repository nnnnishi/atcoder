from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
C = [int(_) for _ in input().split()]
A.sort()
B.sort()


def checkB(n, S):
    idx = bisect_left(S, n)
    return idx


def checkA(n, S):
    idx = bisect_left(S, n)
    return idx


lenA = len(A)
dicB = defaultdict(int)
lenB = len(B)
for c in C:
    dicB[checkB(c, B) - 1] += 1
ans = 0
cnt = 0
for i in range(lenB - 1, -1, -1):
    cnt += dicB[i]
    ans += cnt * checkA(B[i], A)

print(ans)
