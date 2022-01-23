import sys

input = sys.stdin.readline

Y, X = [int(_) for _ in input().split()]
c = [list(input().rstrip()) for _ in range(Y)]
for y in range(Y):
    for x in range(X):
        if c[y][x] == ".":
            check = set()
            for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= y + dy < Y and 0 <= x + dx < X:
                    check.add(c[y + dy][x + dx])
            for i in range(1, 6):
                if str(i) not in check:
                    c[y][x] = str(i)
for i in range(Y):
    print("".join(c[i]))
