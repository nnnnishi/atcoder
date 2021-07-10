from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

K = int(input())
# 最小公約数: greatest common divisor
# GCDは結合則,交換則が成り立ちどこから計算しても変わらない
# code: https://note.nkmk.me/python-gcd-lcm/
# python 3.9からはmath.gcdで複数もいける
# O(log max(a,b))
import math
from functools import reduce

# 2つ以上の最小公約数
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


ans = 0
for i in range(1, K + 1):
    for j in range(1, K + 1):
        for k in range(1, K + 1):
            ans += my_gcd(i, j, k)
print(ans)