from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

C.sort(reverse=True)
B.sort()
A.sort()
b_i = N
a_i = N
# print(A)
# print(B)
# print(C)
ans = 0
for c in C:
    # print(c, "c_check")
    b_check = c
    b_i = bisect_left(B, b_check, lo=0, hi=b_i)
    b_i -= 1
    # print(b_i)
    if b_i < 0:
        exit(print(ans))
    a_check = B[b_i]
    # print(a_check, "b_find")
    a_i = bisect_left(A, a_check, lo=0, hi=a_i)
    a_i -= 1
    if a_i >= 0:
        # print(A[a_i], "a_find")
        ans += 1
    if a_i <= 0 and b_i <= 0:
        exit(print(ans))
    # print(a_i)
print(ans)
