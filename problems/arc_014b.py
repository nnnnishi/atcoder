Y, X = [int(_) for _ in input().split()]
A = [list(map(int, list(input()))) for i in range(Y)]
check = [[1] * X for _ in range(Y)]
ans = [[0] * X for _ in range(Y)]
for y in range(Y - 2):
    for x in range(1, X - 1):
        if A[y][x] != 0:
            ans[y + 1][x] = A[y][x]
            A[y + 2][x] -= A[y][x]
            A[y + 1][x + 1] -= A[y][x]
            A[y + 1][x - 1] -= A[y][x]
            A[y][x] -= A[y][x]

for y in range(Y):
    print("".join(list(map(str, ans[y]))))
