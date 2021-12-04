N, L = [int(_) for _ in input().split()]
query = []
for i in range(L):
    query.append(list(input()))
G = list(input())
# ゴール
for i in range(len(G)):
    if G[i] == "o":
        nx = i
for q in query[::-1]:
    if nx + 2 < len(q) and q[nx + 1] == "-":
        nx = nx + 2
    elif nx - 2 >= 0 and q[nx - 1] == "-":
        nx = nx - 2
    else:
        nx = nx
print(1 + nx // 2)
