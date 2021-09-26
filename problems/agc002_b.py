N, M = [int(_) for _ in input().split()]
c = [0] * N
n = [1] * N
c[0] = 1
query = []
for i in range(M):
    query.append([int(_) for _ in input().split()])

for x, y in query:
    x -= 1
    y -= 1
    n[x] -= 1
    if c[x] == 1:
        c[y] = 1
    n[y] += 1
    if n[x] == 0:
        c[x] = 0

print(sum(c))
