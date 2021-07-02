from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
import numpy as np

N = int(input())
P = "".join(input().split())
Q = "".join(input().split())
check = []
cnt = 0
for s in permutations(P, N):
    cnt += 1
    check.append("".join(s))
check.sort()
pi = -1
qi = -1
for i in range(cnt):
    if check[i] == P:
        pi = i
    if check[i] == Q:
        qi = i
    if pi != -1 and qi != -1:
        exit(print(abs(pi - qi)))
