from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

q = deque()
s = list(input())
N = len(s)
q.append("i")
l = s[0]
ans = N
for i in range(1, N):
    if l == "S" and s[i] == "T":
        ans -= 2
        l = q.pop()
    else:
        q.append(l)
        l = s[i]
print(ans)