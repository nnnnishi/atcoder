from collections import Counter, deque, defaultdict

# O(N+M)
N = int(input())
G = [[] for i in range(N)]

for i in range(N - 1):
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
            Q.append(j)

ans1 = []
ans2 = []
for i in range(N):
    if dist[i] % 2 == 0:
        ans1.append(i + 1)
    else:
        ans2.append(i + 1)
if len(ans1) >= (N // 2):
    print(*ans1[: (N // 2)])
else:
    print(*ans2[: (N // 2)])
