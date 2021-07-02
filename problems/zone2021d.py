from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

S = list(input())
rev = False
T = deque()
for i in range(len(S)):
    if S[i] != "R":
        if len(T) > 0:
            if not rev:
                # みぎ
                check = T.pop()
                if check != S[i]:
                    T.append(check)
                    T.append(S[i])
            # ひだり
            else:
                check = T.popleft()
                if check != S[i]:
                    T.appendleft(check)
                    T.appendleft(S[i])
        else:
            T.append(S[i])

    else:
        if rev == True:
            rev = False
        else:
            rev = True
if rev:
    T.reverse()
print("".join(T))