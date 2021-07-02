from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M, K, S = list(map(int, input().split()))
P, Q = [int(_) for _ in input().split()]
# 危険な街
D = [False] * N
q = deque()
# 通れない街
C = [False] * N
for i in range(K):
    c = int(input())
    C[c - 1] = True
    D[c - 1] = True
    q.append((c - 1, 0))
G = [[] for i in range(N)]
for i in range(M):
    A, B = list(map(int, input().split()))
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)

# 危険な街を判定 幅優先探索
while len(q) > 0:
    i, d = q.popleft()
    for j in G[i]:
        if not D[j] and d + 1 <= S:
            D[j] = True
            q.append((j, d + 1))

# 1からNまでダイクストラ
q = []
done = [False] * N
dist = [-1] * N
dist[0] = 0
heappush(q, (0, 0))
while len(q) > 0:
    d, i = heappop(q)
    if done[i]:
        continue
    done[i] = True
    for g in G[i]:
        if g == N - 1:
            if dist[g] == -1 or dist[g] > d:
                dist[g] = d
            continue
        if not C[g]:
            if D[g]:
                if dist[g] == -1 or dist[g] > d + Q:
                    dist[g] = d + Q
                    heappush(q, (dist[g], g))
            else:
                if dist[g] == -1 or dist[g] > d + P:
                    dist[g] = d + P
                    heappush(q, (dist[g], g))
print(dist[N - 1])
