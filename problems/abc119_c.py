N, A, B, C = [int(_) for _ in input().split()]
l = []
for i in range(N):
    l.append(int(input()))
l.sort()

ans = 10 ** 20


def calc(L):
    cs = 0
    for i in range(3):
        c = 0
        for j in range(len(L[i])):
            c += L[i][j]
            if j > 0:
                cs += 10
        if i == 0:
            cs += abs(A - c)
        elif i == 1:
            cs += abs(B - c)
        else:
            cs += abs(C - c)
    return cs


def dfs(i, L):
    global ans
    if i == N:
        if len(L[0]) != 0 and len(L[1]) != 0 and len(L[2]) != 0:
            ans = min(calc(L), ans)
        return
    else:
        for j in range(4):
            L[j].append(l[i])
            dfs(i + 1, L)
            L[j].remove(l[i])
        return


dfs(0, [[], [], [], []])
print(ans)