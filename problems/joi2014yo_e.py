from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, K = [int(_) for _ in input().split()]
C = []
R = []
for i in range(N):
    c, r = [int(_) for _ in input().split()]
    C.append(c)
    R.append(r)
G = [[] for i in range(N)]
for j in range(K):
    A, B = [int(_) for _ in input().split()]
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)

# ある点から幅優先でコストをつける
def calc_dist(i):
    q = deque()
    dist = [-1] * N
    dist[i] = 0
    q.append((0, i, R[i]))
    while len(q) > 0:
        d, j, r = q.popleft()
        for g in G[j]:
            if dist[g] == -1:
                dist[g] = C[i]
                if r - 1 > 0:
                    q.append((dist[g], g, r - 1))
    return dist


# ダイクストラでNまでいく
q = []
done = [False] * N
distD = [-1] * N
distD[0] = 0
heappush(q, (0, 0))
while len(q) > 0:
    d, i = heappop(q)
    if i == N - 1:
        exit(print(distD[N - 1]))
    if done[i]:
        continue
    done[i] = True
    dist_L = calc_dist(i)
    for g in range(N):
        if dist_L[g] != -1:
            if distD[g] == -1 or distD[g] > distD[i] + dist_L[g]:
                distD[g] = distD[i] + dist_L[g]
                heappush(q, (distD[g], g))
