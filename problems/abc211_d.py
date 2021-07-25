from collections import Counter, deque, defaultdict

N, M = [int(_) for _ in input().split()]
MOD = 10 ** 9 + 7
# O(N+M)
G = [[] for i in range(N)]

for i in range(M):
    a, b = [int(_) for _ in input().split()]
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


# 幅優先
num = [0] * N
dist = [-1] * N
Q = deque()
Q.append(0)
dist[0] = 0
num[0] = 1
while len(Q) > 0:
    # 4辺チェックしキューへ追加
    i = Q.popleft()
    for j in G[i]:
        if dist[j] == -1 or dist[j] > dist[i] + 1:
            dist[j] = dist[i] + 1
            num[j] = num[i]
            Q.append(j)
        elif dist[j] == dist[i] + 1:
            num[j] += num[i]
            num[j] %= MOD

print(num[N - 1] % MOD)
