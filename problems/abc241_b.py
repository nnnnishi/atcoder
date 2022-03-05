from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
d = Counter(A)
for b in B:
    if b not in d or d[b] == 0:
        print("No")
        exit()
    else:
        d[b] -= 1
print("Yes")

