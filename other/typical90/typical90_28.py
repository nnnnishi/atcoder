# 2次元累積和
# https://atcoder.jp/contests/typical90/tasks/typical90_ab
# https://twitter.com/e869120/status/1388262816101007363/photo/1
import sys

input = sys.stdin.readline

N = int(input())
maxX = 1000
maxY = 1000
A = [[0] * (maxX + 1) for _ in range(maxY + 1)]
for i in range(N):
    lx, ly, rx, ry = [int(_) for _ in input().split()]
    A[ly][lx] += 1
    A[ry][rx] += 1
    A[ly][rx] -= 1
    A[ry][lx] -= 1


# x方向の累積和
for y in range(maxY + 1):
    for x in range(1, maxX + 1):
        A[y][x] += A[y][x - 1]

# y方向の累積和
for x in range(maxX + 1):
    for y in range(1, maxY + 1):
        A[y][x] += A[y - 1][x]

# x,yで重なる枚数をansとする
ans = [0] * (N + 1)
# x,y ともに0スタート
for x in range(maxX + 1):
    for y in range(maxY + 1):
        ans[A[y][x]] += 1
"""
for a in A[:7]:
    print(a[:7])
print()
"""
# 重なる枚数の面積を列挙
for i in range(1, N + 1):
    print(ans[i])

