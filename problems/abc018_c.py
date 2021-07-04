y, x, k = [int(_) for _ in input().split()]
s = [list(input()) for i in range(y)]
# print(s)
A = [[1] * x for i in range(y)]
# print(A)
for i in range(y):
    for j in range(x):
        if s[i][j] == "x":
            for dy in range(-k + 1, k):
                for dx in range(-k + 1, k):
                    if (
                        0 <= i + dy <= y - 1
                        and 0 <= j + dx <= x - 1
                        and abs(dx) + abs(dy) <= k - 1
                    ):
                        A[i + dy][j + dx] = 0
# print(A)
print(sum([sum(A[dy][k - 1 : x - k + 1]) for dy in range(k - 1, y - k + 1)]))
