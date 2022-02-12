from collections import Counter, deque, defaultdict

N = 10
G = [[] for i in range(N)]

for i in range(N - 1):
    a, b = [int(_) for _ in input().split()]
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def bfs(start):
    """
    O(N+M)
    """
    dist = [-1] * N
    Q = deque()
    Q.append(start)
    dist[start] = 0
    while len(Q) > 0:
        # 4辺チェックしキューへ追加
        i = Q.popleft()
        for j in G[i]:
            if dist[j] == -1 or dist[j] > dist[i] + 1:
                dist[j] = dist[i] + 1
                Q.append(j)
    return dist
