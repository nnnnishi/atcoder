from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, K = [int(_) for _ in input().split()]
S = list(input())
L = sorted(list(set(S)))
pre = [[N] * (N + 1) for _ in range(len(L))]
for i in range(N - 1, -1, -1):
    for j in range(len(L)):
        if S[i] == L[j]:
            pre[j][i] = i
        else:
            pre[j][i] = pre[j][i + 1]
# print(pre)
idx = 0
res = K
ans = []
while idx < N:
    for l in range(len(L)):
        if pre[l][idx] < N - res + 1:
            ans.append(L[l])
            res -= 1
            if res == 0:
                print("".join(ans))
                exit()
            idx = pre[l][idx] + 1
            break
