import math
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort


N = int(input())
ml = int(math.sqrt(10 ** 9) // 1)
c_set = set()
for i in range(1, ml + 1):
    c_set.add(i ** 2)
    c_set.add(i ** 3)
c_l = list(c_set)
c_l.sort()

for _ in range(N):
    x = int(input())
    print(bisect(c_l, x))
