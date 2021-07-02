K, X = [int(_) for _ in input().split()]
print(*[i for i in range(X - (K - 1), X + K)])
