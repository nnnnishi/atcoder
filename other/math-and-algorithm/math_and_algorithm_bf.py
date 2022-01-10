import sys

input = sys.stdin.readline
N = int(input())
L = []
for _ in range(N):
    L.append([int(_) for _ in input().split()])
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        x = (L[i][2] * L[j][1] - L[j][2] * L[i][1]) / (
            L[i][0] * L[j][1] - L[i][1] * L[j][0]
        )
        y = (-L[j][0] * L[i][2] + L[i][0] * L[j][2]) / (
            L[i][0] * L[j][1] - L[i][1] * L[j][0]
        )
        if x + y > ans:
            ok = True
            for k in range(N):
                if L[k][0] * x + L[k][1] * y > L[k][2]:
                    ok = False
            if ok:
                ans = x + y
print(ans)
