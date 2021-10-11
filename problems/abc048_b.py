a, b, x = [int(_) for _ in input().split()]

nb = b // x
na = (a - 1) // x

print(nb - na)
