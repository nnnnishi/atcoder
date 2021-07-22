N, M = [int(_) for _ in input().split()]
L = []
R = []
for i in range(M):
    l, r = [int(_) for _ in input().split()]
    L.append(l)
    R.append(r)
print(max(min(R) - max(L) + 1, 0))
