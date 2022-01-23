A, B = [int(_) for _ in input().split()]
for x in range(-100, 101):
    for y in range(-100, 101):
        if x + y == A and x - y == B:
            print(x, y)
            exit()
