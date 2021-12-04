ord = [int(_) for _ in input().split()]
N = int(input())
oris = []
for i in range(N):
    oris.append(input())

d = {}
d["0"] = "0"
for i in range(1, len(ord)):
    # ori -> ch
    d[str(ord[i])] = str(str(i))


def conv(i):
    return d[i]


ans = []
for i in range(N):
    ori = oris[i]
    ch = "".join(list(map(conv, list(ori))))
    # (ch,ori)で結合
    ans.append([int(ch), int(ori)])

# chのせかいでソート
ans.sort()

for i in range(N):
    print(ans[i][1])
