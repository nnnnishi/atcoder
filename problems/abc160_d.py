from collections import Counter, deque, defaultdict

# O(N+M)
N, X, Y = [int(_) for _ in input().split()]
G = [[] for i in range(N)]

for i in range(N - 1):
    G[i].append(i + 1)
    G[i + 1].append(i)
G[X - 1].append(Y - 1)
G[Y - 1].append(X - 1)


def dfs(s):
    """
    O(N+M)
    """
    # 幅優先
    dist = [-1] * N
    Q = deque()
    Q.append(s)
    dist[s] = 0
    while len(Q) > 0:
        # 4辺チェックしキューへ追加
        i = Q.popleft()
        for j in G[i]:
            if dist[j] == -1 or dist[j] > dist[i] + 1:
                dist[j] = dist[i] + 1
                Q.append(j)
    return dist


ans = [0] * (N - 1)
for i in range(N):
    d = dfs(i)
    for j in range(i + 1, N):
        ans[d[j] - 1] += 1
for i in range(N - 1):
    print(ans[i])
