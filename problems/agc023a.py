from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [int(_) for _ in input().split()]
sumA = [A[0]] * (len(A))
for i in range(1, len(A)):
    sumA[i] = sumA[i - 1] + A[i]
dic = defaultdict(int)
for i in sumA + [0]:
    dic[i] += 1
ans = 0
for i in dic:
    ans += (dic[i] * (dic[i] - 1)) // 2
print(ans)