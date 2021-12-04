from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
for _ in range(N):
    c = [int(_) for _ in input().split()]
    ans = 0
    viewed = set()
    ischeck = True
    while ischeck:
        if len(set(c)) <= 2:
            d = defaultdict(int)
            for i in range(3):
                d[c[i]] += 1
            for i in range(3):
                if d[c[i]] >= 2:
                    ischeck = False
                    print(ans + c[i])
                    break
        else:
            c.sort()
            pat = " ".join(map(str, c))
            if pat in viewed:
                ischeck = False
                print(-1)
            else:
                viewed.add(pat)
                sa0 = c[1] - c[0]
                sa1 = c[2] - c[0]
                sa2 = c[2] - c[1]
                if sa0 % 3 == 0:
                    if sa0 >= 3:
                        mul = sa0 // 3
                        c[0] += mul * 2
                        c[1] -= mul
                        c[2] -= mul
                        ans += mul
                elif sa1 % 3 == 0:
                    if sa1 >= 3:
                        mul = sa1 // 3
                        c[0] += mul * 2
                        c[1] -= mul
                        c[2] -= mul
                        ans += mul
                elif sa2 % 3 == 0:
                    if sa1 >= 3:
                        mul = sa1 // 3
                        c[0] += mul * 2
                        c[1] -= mul
                        c[2] -= mul
                        ans += mul
                else:
                    ischeck = False
                    print(-1)
