from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

S = list(input())
K = int(input())
fill = deque()
ans = 0
tmp = 0
for i in range(len(S)):
    if S[i] == ".":
        if len(fill) < K:
            fill.append(i)
            tmp += 1
        else:
            if tmp > ans:
                ans = tmp
            if len(fill) >= 1:
                j = fill.popleft()
                fill.append(i)
                tmp = i - j
            else:
                tmp = 0
    else:
        tmp += 1

if tmp > ans:
    ans = tmp

print(ans)
