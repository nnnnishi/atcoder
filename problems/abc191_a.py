V, T, S, D = [int(_) for _ in input().split()]
if V * T <= D <= V * S:
    print("No")
else:
    print("Yes")

