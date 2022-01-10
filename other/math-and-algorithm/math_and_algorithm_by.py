a, b, c = [int(_) for _ in input().split()]
if b == 1:
    if a < c:
        print("Yes")
    else:
        print("No")
    exit()
else:
    if c == 1:
        exit(print("No"))
    else:
        nc = c
        for _ in range(b - 1):
            nc *= c
            if nc > a:
                exit(print("Yes"))
print("No")

