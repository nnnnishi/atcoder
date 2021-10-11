from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge

N, M, X, Y = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for i in range(M):
    a, b, t, k = [int(_) for _ in input().split()]
    graph[a - 1].append([t, k, b - 1])
    graph[b - 1].append([t, k, a - 1])

ans = 0
s = 0
dist = [-1] * N
done = [False] * N
Q = [(0, X - 1)]
dist[X - 1] = 0
while len(Q) > 0:
    d, i = heappop(Q)
    if done[i]:
        continue
    for t, k, j in graph[i]:
        if dist[i] % k == 0:
            c = t
        else:
            c = t + k - (dist[i] % k)
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heappush(Q, (dist[j], j))
    done[i] = True
if dist[Y - 1] != -1:
    print(dist[Y - 1])
else:
    print(-1)
