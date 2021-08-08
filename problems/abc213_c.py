Y, X, N = list(map(int, input().split()))
query = []
xset = set()
yset = set()
for i in range(N):
    y, x = [int(_) for _ in input().split()]
    xset.add(x)
    yset.add(y)
    query.append([y, x])
xl = list(xset)
yl = list(yset)
xl.sort()
yl.sort()
dx = {}
dy = {}
for i in range(len(xl)):
    dx[xl[i]] = i + 1
for i in range(len(yl)):
    dy[yl[i]] = i + 1

for y, x in query:
    print(dy[y], dx[x])
