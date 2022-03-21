from operator import itemgetter

N = int(input())
q = []
for _ in range(N):
    q.append(list(map(int, input().split())))
S = list(input())
for i in range(N):
    q[i].append(S[i])
q.sort(key=itemgetter(1, 0))
py = -1
px = -1
pd = "-"
for i in range(N):
    x, y, d = q[i]
    # yの一致を確認
    if py != y:
        px = x
        py = y
        pd = d
    else:
        # yの一致
        if pd == "R" and d == "L":
            print("Yes")
            exit()
        else:
            px = x
            py = y
            pd = d
print("No")
