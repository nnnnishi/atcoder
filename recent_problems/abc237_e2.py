from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge

N, M = list(map(int, input().split()))
H = [int(_) for _ in input().split()]
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = [int(_) for _ in input().split()]
    if H[a - 1] >= H[b - 1]:
        graph[a - 1].append([-1 * (H[a - 1] - H[b - 1]), b - 1])
        graph[b - 1].append([2 * (H[a - 1] - H[b - 1]), a - 1])
    else:
        # - 楽しさ
        graph[a - 1].append([-2 * (H[a - 1] - H[b - 1]), b - 1])
        graph[b - 1].append([1 * (H[a - 1] - H[b - 1]), a - 1])

INF = 10 ** 20
ans = 0
s = 0
dist = [INF] * N
Q = [(0, s)]
dist[s] = 0
while len(Q) > 0:
    d, i = heappop(Q)
    if dist[i] < d:
        continue
    for g in graph[i]:
        j = g[1]
        c = g[0]
        if dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heappush(Q, (dist[j], j))

    # print(dist)
ans = -min(dist)
# print(dist)
print(ans)
