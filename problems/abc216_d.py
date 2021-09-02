from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations


N, M = list(map(int, input().split()))
k_l = {}
for i in range(M):
    k = int(input())
    k_l[i] = deque([int(_) for _ in input().split()])
c = [-1] * N
cnt = 2 * N
i = 0
f_num = 0
back = deque()
force = False
while f_num < M:
    force = False
    if len(k_l[i]) == 0:
        f_num += 1
    else:
        e = k_l[i].pop()
        e -= 1
        if c[e] != -1:
            cnt -= 2
            if cnt == 0:
                exit(print("Yes"))
            # あとでもどる
            back.appendleft(i)
            # iにもどる
            force = True
            i = c[e]
            f_num -= 1
        else:
            c[e] = i
            f_num += 1

    if force:
        continue
    else:
        if len(back) > 0:
            i = back.popleft()
        else:
            i += 1
            i %= M
    # print("k", k_l)
    # print("m", m)
    # print("c", cnt)
print("No")
