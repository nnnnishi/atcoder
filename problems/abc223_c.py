from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
q = []
ori_q = []
tq = []
for i in range(N):
    a, b = [int(_) for _ in input().split()]
    q.append(a)
    ori_q.append(a)
    tq.append(b)

l = 0
r = N - 1
last = "l"
if N == 1:
    exit(print(q[0] / 2))

while l != r:
    # ひだりのけいさん
    l_long = q[l]
    l_time = tq[l]
    l_at = l_long / l_time
    # みぎのけいさん
    r_long = q[r]
    r_time = tq[r]
    r_at = r_long / r_time
    if l_at >= r_at:
        # lののこり
        q[l] = l_long - r_at * l_time
        r -= 1
        last = "r"
    else:
        # rののこり
        q[r] = r_long - l_at * r_time
        l += 1
        last = "l"

ans = 0
if q[l] == 0:
    for i in range(l + 1):
        ans += ori_q[i]
else:
    for i in range(l):
        ans += ori_q[i]

    if last == "l":
        ans += q[l] - q[l] / 2
    else:
        ans += ori_q[l] - (q[l] / 2)
print(ans)
