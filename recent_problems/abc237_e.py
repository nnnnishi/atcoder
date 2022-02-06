from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge

N, M = list(map(int, input().split()))
H = [int(_) for _ in input().split()]
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = [int(_) for _ in input().split()]
    if H[a - 1] >= H[b - 1]:
        # - 楽しさ
        c = 0
        graph[a - 1].append([c, b - 1])
        c = H[a - 1] - H[b - 1]
        graph[b - 1].append([c, a - 1])
    else:
        # - 楽しさ
        c = H[b - 1] - H[a - 1]
        graph[a - 1].append([c, b - 1])
        c = 0
        graph[b - 1].append([c, a - 1])


ans = 0
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

ans = 0
for i in range(N):
    if dist[i] != -1:
        if ans < -dist[i] + H[0] - H[i]:
            ans = -dist[i] + H[0] - H[i]
# print(dist)
print(ans)
