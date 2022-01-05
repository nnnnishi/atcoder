from collections import Counter, deque, defaultdict

# O(N+M)
N, M = [int(_) for _ in input().split()]
G = [[] for i in range(N)]
L = []
for i in range(M):
    L.append([int(_) for _ in input().split()])
L.sort()
for a, b in L:
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
ans = 0
for i in range(N):
    cnt = 0
    for j in G[i]:
        if j < i:
            cnt += 1
        if cnt > 2:
            break
        if j > i:
            break
    if cnt == 1:
        ans += 1
print(ans)
