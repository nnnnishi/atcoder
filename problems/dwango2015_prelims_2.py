from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

S = list(input())
cnt = 0
ans = 0
i = 0
while i < len(S) - 1:
    if S[i] + S[i + 1] == "25":
        cnt += 1
        i += 2
    else:
        if cnt > 0:
            while cnt > 0:
                ans += cnt
                cnt -= 1
        i += 1

if cnt > 0:
    while cnt > 0:
        ans += cnt
        cnt -= 1
print(ans)
