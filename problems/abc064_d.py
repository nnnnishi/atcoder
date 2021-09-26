from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
S = list(input())
q = deque()
cnt = 0
for s in S:
    if s == "(":
        cnt += 1
    else:
        cnt -= 1
    if cnt > 0:
        q.append(s)
    elif cnt < 0:
        q.append(s)
        q.appendleft("(")
        cnt += 1
    elif cnt == 0:
        q.append(s)

if cnt > 0:
    for i in range(cnt):
        q.append(")")
else:
    for i in range(-cnt):
        q.append("(")

ans = "".join(list(q))

print(ans)
