from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
fd = defaultdict(int)
ld = defaultdict(int)


for i in range(1, N + 1):
    f = str(i)[0]
    l = str(i)[-1]
    fd[f + " " + l] += 1
    ld[l + " " + f] += 1

ans = 0
for k in fd.keys():
    ans += fd[k] * ld[k]
print(ans)
