from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge

# O(N+M)
N, M = [int(_) for _ in input().split()]

graph = [[] for _ in range(N)]
for i in range(M):
    a, b, c = [int(_) for _ in input().split()]
    graph[a - 1].append([c, b - 1])
    graph[b - 1].append([c, a - 1])

ans = [0] * N

s = 0
dist = [-1] * N
done = [False] * N
Q = [(0, s)]
dist[s] = 0
while len(Q) > 0:
    d, i = heappop(Q)
    if done[i]:
        continue
    for g in graph[i]:
        j = g[1]
        c = g[0]
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heappush(Q, (dist[j], j))
    done[i] = True

for i in range(N):
    ans[i] += dist[i]

s = N - 1
dist = [-1] * N
done = [False] * N
Q = [(0, s)]
dist[s] = 0
while len(Q) > 0:
    d, i = heappop(Q)
    if done[i]:
        continue
    for g in graph[i]:
        j = g[1]
        c = g[0]
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heappush(Q, (dist[j], j))
    done[i] = True


for i in range(N):
    ans[i] += dist[i]

for i in range(N):
    print(ans[i])
