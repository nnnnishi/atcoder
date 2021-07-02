A, B, K = [int(_) for _ in input().split()]
LA = max(0, A - K)
LB = max(0, B - (K - (A - LA)))
print(LA, LB)
