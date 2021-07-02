N, M = list(map(int, input().split()))

q = []
dicP = {}
for _ in range(M):
    P, Y = list(map(int, input().split()))
    dicP.setdefault(P, [])
    dicP[P].append(Y)
    q.append([P, Y])
dicC = {}
for p in dicP:
    l = list(set(dicP[p]))
    l.sort()
    for i, a in enumerate(l):
        dicC.setdefault(p, {})
        dicC[p][a] = i + 1

for p, y in q:
    print(str(p).zfill(6) + str(dicC[p][y]).zfill(6))
