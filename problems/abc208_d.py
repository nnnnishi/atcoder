from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for i in range(M):
    a, b, c = [int(_) for _ in input().split()]
    graph[a - 1].append([c, b - 1])


def calc(k):
    global ans
    # ダイクストラ
    # sとtがkまでまとめてやる
    for s in range(k + 1):
        # k以下の頂点
        dist = [-1] * N
        done = [False] * N
        Q = [(0, s)]
        dist[s] = 0
        while len(Q) > 0:
            d, i = heappop(Q)
            if done[i]:
                continue
            for g in graph[i]:
                if g[1] <= k:
                    j = g[1]
                    c = g[0]
                    if dist[j] == -1 or dist[j] > dist[i] + c:
                        dist[j] = dist[i] + c
                        heappush(Q, (dist[j], j))
                    done[i] = True

        for t in range(k + 1):
            if dist[t] != -1:
                ans += dist[t]
        # tがk以上のときは個別にやる
        for t in range(k + 1, N):
            # k以下の頂点
            dist = [-1] * N
            done = [False] * N
            Q = [(0, s)]
            dist[s] = 0
            while len(Q) > 0:
                d, i = heappop(Q)
                if done[i]:
                    continue
                for g in graph[i]:
                    # k以下のノードのみつかう
                    if g[1] <= k or g[1] == t:
                        j = g[1]
                        c = g[0]
                        if dist[j] == -1 or dist[j] > dist[i] + c:
                            dist[j] = dist[i] + c
                            heappush(Q, (dist[j], j))
                    done[i] = True
            if dist[t] != -1:
                ans += dist[t]
    # s,t がk以上のときは
    for s in range(k + 1, N):
        for t in range(N):
            if s != t:
                # k以下の頂点
                dist = [-1] * N
                done = [False] * N
                Q = [(0, s)]
                dist[s] = 0
                while len(Q) > 0:
                    d, i = heappop(Q)
                    if done[i]:
                        continue
                    for g in graph[i]:
                        # k以下のノードのみつかう
                        if g[1] <= k or g[1] == t:
                            j = g[1]
                            c = g[0]
                            if dist[j] == -1 or dist[j] > dist[i] + c:
                                dist[j] = dist[i] + c
                                heappush(Q, (dist[j], j))
                        done[i] = True
                if dist[t] != -1:
                    ans += dist[t]


ans = 0
for k in range(N):
    calc(k)
print(ans)