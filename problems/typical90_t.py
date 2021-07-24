a, b, c = [int(_) for _ in input().split()]
eps = 10 ** -5
if c == 1:
    print("No")
else:
    t = c
    for i in range(b):
        if a < t:
            exit(print("Yes"))
        t *= c
    print("No")
