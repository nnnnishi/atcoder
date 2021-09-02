Y, X = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for i in range(Y)]
B = [[int(_) for _ in input().split()] for i in range(Y)]

ans = 0
for y in range(Y - 1):
    for x in range(X - 1):
        d = B[y][x] - A[y][x]
        for y2, x2 in [[y + 1, x], [y, x], [y + 1, x + 1], [y, x + 1]]:
            B[y2][x2] -= d
        ans += abs(d)
    if A[y][x + 1] != B[y][x + 1]:
        exit(print("No"))
for x in range(X):
    if A[Y - 1][x] != B[Y - 1][x]:
        exit(print("No"))
print("Yes")
print(ans)
