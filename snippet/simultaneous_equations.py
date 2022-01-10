"""
以下の連立方程式の解x,yをもとめる
a1x + b1y = c1
a2x + b2y = c2
"""
import sys

input = sys.stdin.readline


def solve_SE(a1, b1, c1, a2, b2, c2):
    x = (c1 * b2 - c2 * b1) / (a1 * b2 - b1 * a2)
    y = (-a2 * c1 + a1 * c2) / (a1 * b2 - b1 * a2)
    return x, y


N = int(input())
L = []
for _ in range(N):
    L.append([int(_) for _ in input().split()])
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        x, y = solve_SE(L[i][0], L[i][1], L[i][2], L[j][0], L[j][1], L[j][2])
        if x + y > ans:
            ok = True
            for k in range(N):
                if L[k][0] * x + L[k][1] * y > L[k][2]:
                    ok = False
            if ok:
                ans = x + y
print(ans)
