N, M = [int(_) for _ in input().split()]
t = M * 1900 + (N - M) * 100
print(t * (2 ** M))
