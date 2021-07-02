from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

dic = defaultdict(int)
S = list(input())
for s in S:
    dic[s] += 1
ok = dic["o"]
ng = dic["x"]
if ok > 4:
    exit(print(0))


def check(num, ok, ng):
    num = str(num).zfill(4)
    # print(num)
    sSet = set()
    ngSet = set()
    for ngn in range(9, 9 - ng, -1):
        ngSet.add(ngn)
    # print(ngSet)
    for s in list(num):
        if int(s) in ngSet:
            return 0
        sSet.add(int(s))
    # print(sSet)
    for i in range(ok):
        if i not in sSet:
            return 0
    return 1


ans = 0
for num in range(10000):
    ans += check(num, ok, ng)
print(ans)