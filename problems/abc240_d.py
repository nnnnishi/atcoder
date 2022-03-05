from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
A = list(map(int, input().split()))
q = deque()
ans = 0
for a in A:
    k = a
    if len(q) == 0:
        q.append((a, 1))
        ans = 1
        print(ans)
    else:
        b, num = q.pop()
        if num + 1 == k and a == b:
            ans -= num
            print(ans)
        elif a == b and num + 1 != k:
            q.append((a, num + 1))
            ans += 1
            print(ans)
        else:
            q.append((b, num))
            q.append((a, 1))
            ans += 1
            print(ans)

