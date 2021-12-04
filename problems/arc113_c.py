from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

S = list(input())
N = len(S)
ans = 0
cnt = 0
b_s = ""
res = 0
d = defaultdict(int)
for i in range(N):
    if S[N - 1 - i] == b_s:
        for k in d.keys():
            if k != b_s:
                ans += d[k]
        d = defaultdict(int)
        d[b_s] += i + 1
    else:
        d[S[N - 1 - i]] += 1
    b_s = S[N - 1 - i]

print(ans)
