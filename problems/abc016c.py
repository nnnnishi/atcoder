N, M = [int(_) for _ in input().split()]
dic = {}
inv_dic = {}
fdic = {}
for i in range(N):
    dic[i + 1] = i
    inv_dic[i] = i + 1
    fdic[i] = set()
A = []
B = []
F = []
for i in range(M):
    a, b = [int(_) for _ in input().split()]
    F += [(dic[a], dic[b]), (dic[b], dic[a])]

for f in F:
    fdic[f[0]].add(f[1])

for i in range(N):
    # 友達の友達の集合 - 友達の集合
    aset = set()
    for f in fdic[i]:
        aset = aset | fdic[f]
    # 友達を除く
    for k in fdic[i]:
        if k in aset:
            aset.remove(k)
    # 自分を除く
    if i in aset:
        aset.remove(i)
    print(len(aset))
