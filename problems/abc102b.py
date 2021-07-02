N = int(input())
Xmax = (N // 4) + 1
Ymax = (N // 7) + 1
for x in range(Xmax):
    for y in range(Ymax):
        if 4 * x + 7 * y == N:
            exit(print("Yes"))
print("No")