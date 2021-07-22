from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, K = list(map(int, input().split()))
c = [int(_) for _ in input().split()]
cntc = Counter(c[:K])
# 最初の種類
t = len(cntc)
ans = t
for i in range(K, N):
    # ひく
    cntc[c[i - K]] -= 1
    if cntc[c[i - K]] == 0:
        t -= 1
    # たす
    cntc[c[i]] += 1
    if cntc[c[i]] == 1:
        t += 1
    ans = max(ans, t)
print(ans)