N, M = [int(_) for _ in input().split()]


def conv(a):
    astr = list(str(a))
    astr.sort()
    ac = int("".join(astr)[::-1]) - int("".join(astr))
    return ac


a = N
b = N
for i in range(M):
    a = conv(a)
    if b == a:
        exit(print(a))
    b = a
print(a)