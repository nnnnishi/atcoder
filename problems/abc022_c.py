from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge

N, M = [int(_) for _ in input().split()]

dist = [[-1] * N for i in range(N)]
for i in range(N):
    dist[i][i] = 0

graph = [[] for _ in range(N)]
for i in range(M):
    a, b, c = [int(_) for _ in input().split()]
    graph[a - 1].append([c, b - 1])
    graph[b - 1].append([c, a - 1])


def dy(s):
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
            if not (i == s and j == 0):
                if dist[j] == -1 or dist[j] > dist[i] + c:
                    dist[j] = dist[i] + c
                    heappush(Q, (dist[j], j))
        done[i] = True
    return dist[0]


ans = 10 ** 10
for s in graph[0]:
    tmp = dy(s[1]) + s[0]
    check = dy(s[1])
    if check != -1:
        ans = min(ans, tmp)
if ans != 10 ** 10:
    print(ans)
else:
    print(-1)