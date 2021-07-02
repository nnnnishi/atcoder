from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = [int(_) for _ in input().split()]
s = [[int(_) for _ in input().split()] for i in range(M)]
p = [int(_) for _ in input().split()]


def has_bit(n, j):
    return (n & (1 << j)) > 0


# onになっているスイッチの組み合わせ:2^n(1<<N)通り
ans = 0
for n in range(1 << N):
    for m in range(M):
        # sMがonになってる個数を数える
        cnt = 0
        for j in s[m][1:]:
            if has_bit(n, j - 1):
                cnt += 1
        if cnt % 2 != p[m]:
            break
        if m == M - 1:
            ans += 1
print(ans)
