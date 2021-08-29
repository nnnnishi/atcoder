from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
S = list(input())
# i 以降のR,G,Bの合計を前処理
c = Counter(S)
d = {}
for s in ["R", "G", "B"]:
    d[s] = []
for i in range(N):
    c[S[i]] -= 1
    for s in ["R", "G", "B"]:
        d[s].append(c[s])


ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        cs = set(["R", "G", "B"]) - set([S[i], S[j]])
        if len(cs) == 1:
            ans += d[list(cs)[0]][j]
            if j + (j - i) <= N - 1 and S[j + (j - i)] == list(cs)[0]:
                ans -= 1

print(ans)
