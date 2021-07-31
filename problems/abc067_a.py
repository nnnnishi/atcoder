A, B = [int(_) for _ in input().split()]
for x in [A, B, A + B]:
    if x % 3 == 0:
        exit(print("Possible"))
print("Impossible")
