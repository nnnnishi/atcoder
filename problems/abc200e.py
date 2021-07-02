from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, K = list(map(int, input().split()))

# 和のDP
cnt = []
for _ in range(3):
    cnt.append([0] * (3 * N + 1))

idx = 0
for n in range(1, N + 1):
    cnt[idx][n] = 1

# cnt の累積和
idx = 1
cum = []
sum_c = 0
for i in range(3 * N + 1):
    sum_c += cnt[idx - 1][i]
    cum.append(sum_c)

for i in range(3 * N + 1):
    start = i - N - 1
    end = i - 1
    if start <= 0:
        start = 0
    if end <= 0:
        end = 0
    cnt[idx][i] = cum[end] - cum[start]

# cnt の累積和
idx = 2
cum = []
sum_c = 0
for i in range(3 * N + 1):
    sum_c += cnt[idx - 1][i]
    cum.append(sum_c)


for i in range(3 * N + 1):
    start = i - N - 1
    end = i - 1
    if start <= 0:
        start = 0
    if end <= 0:
        end = 0
    cnt[idx][i] = cum[end] - cum[start]
# idx2に関して累積和3
cum = []
sum_c = 0
for i in range(3 * N + 1):
    sum_c += cnt[idx][i]
    cum.append(sum_c)

wa = bisect_left(cum, K)
rest = K - cum[wa - 1]
# print(wa, rest)
# きれいさ
for ki in range(1, N + 1):
    # print(ki)
    T = wa - ki
    # kiがその値で実行可能か -> だめなら残りを消費せずkiを+1
    if T - 1 <= 2 * N - T + 1:
        pat = T - 1
        # print("pat", pat, rest)
        if rest - pat <= 0:
            ni = 1 + (pat - rest)
            oi = wa - ki - ni
            exit(print(ki, oi, ni))
        # そのkiでのこりを消費できるか
        # -> 消費できたら ki, 1+rest3, wa-ki-(1+rest)
        # -> だめなら N-(rest-1)消費して次のkiへ
    else:
        pat = 2 * N - T + 1
        # print("pat", pat, rest)
        if rest - pat <= 0:
            oi = N - (pat - rest)
            ni = wa - ki - oi
            exit(print(ki, oi, ni))
    if pat >= 1:
        rest -= pat
