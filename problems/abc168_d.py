from collections import Counter, deque, defaultdict

N, M = [int(_) for _ in input().split()]
# O(N+M)
G = [[] for i in range(N)]
B = [-1 for i in range(N)]
for i in range(M):
    a, b = [int(_) for _ in input().split()]
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


# 幅優先
dist = [-1] * N
Q = deque()
Q.append(0)
dist[0] = 0
while len(Q) > 0:
    # 4辺チェックしキューへ追加
    i = Q.popleft()
    for j in G[i]:
        if dist[j] == -1 or dist[j] > dist[i] + 1:
            dist[j] = dist[i] + 1
            B[j] = i + 1
            Q.append(j)
print("Yes")
for i in range(1, N):
    print(B[i])