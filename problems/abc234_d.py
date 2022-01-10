from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge


import sys

input = sys.stdin.readline

N, K = [int(_) for _ in input().split()]
P = [int(_) for _ in input().split()]
Q = P[:K].copy()
Q.sort()
heapify(Q)
print(Q[0])
for i in range(K, N):
    if P[i] < Q[0]:
        print(Q[0])
    else:
        heappop(Q)
        heappush(Q, P[i])
        print(Q[0])

