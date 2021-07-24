from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge

N, M, T = list(map(int, input().split()))
A = [int(_) for _ in input().split()]
graph = [[] for _ in range(N)]
graph2 = [[] for _ in range(N)]
for i in range(M):
    a, b, c = [int(_) for _ in input().split()]
    graph[a - 1].append([c, b - 1])
    graph2[b - 1].append([c, a - 1])

s = 0
dist1 = [-1] * N
done = [False] * N
Q = [(0, s)]
dist1[s] = 0
while len(Q) > 0:
    d, i = heappop(Q)
    if done[i]:
        continue
    for g in graph[i]:
        j = g[1]
        c = g[0]
        if dist1[j] == -1 or dist1[j] > dist1[i] + c:
            dist1[j] = dist1[i] + c
            heappush(Q, (dist1[j], j))
    done[i] = True


s = 0
dist2 = [-1] * N
done = [False] * N
Q = [(0, s)]
dist2[s] = 0
while len(Q) > 0:
    d, i = heappop(Q)
    if done[i]:
        continue
    for g in graph2[i]:
        j = g[1]
        c = g[0]
        if dist2[j] == -1 or dist2[j] > dist2[i] + c:
            dist2[j] = dist2[i] + c
            heappush(Q, (dist2[j], j))
    done[i] = True

ans = 0
for i in range(N):
    if dist1[i] != -1 and dist2[i] != -1:
        if T - (dist1[i] + dist2[i]) > 0:
            ans = max((T - (dist1[i] + dist2[i])) * A[i], ans)
print(ans)