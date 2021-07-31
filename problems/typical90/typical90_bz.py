N, M = [int(_) for _ in input().split()]
l = [0] * N
for i in range(M):
    a, b = [int(_) for _ in input().split()]
    c = max(a, b)
    l[c - 1] += 1
ans = 0
for i in range(N):
    if l[i] == 1:
        ans += 1
print(ans)
