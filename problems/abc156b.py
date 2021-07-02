N, R = [int(_) for _ in input().split()]

if N >= 10:
    print(R)
else:
    print(R + 100 * (10 - N))
