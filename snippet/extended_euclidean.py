a, b = [int(_) for _ in input().split()]
# Extended Euclidean Algorithm
def extgcd(a, b):
    if b != 0:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0


d, x, y = extgcd(a, b)
print(x, y)
