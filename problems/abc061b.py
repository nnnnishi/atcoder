N, M = [int(_) for _ in input().split()]
a = []
b = []
edge = [0] * N
for i in range(M):
    ai, bi = [int(_) for _ in input().split()]
    edge[ai - 1] += 1
    edge[bi - 1] += 1

for x in edge:
    print(x)
