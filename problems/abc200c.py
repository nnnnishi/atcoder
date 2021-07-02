from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))
dic = defaultdict(int)
for a in A:
    dic[a % 200] += 1
ans = 0
for k in dic:
    ans += dic[k] * (dic[k] - 1) // 2
print(ans)