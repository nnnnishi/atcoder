N, x, y = [int(_) for _ in input().split()]

if abs(x) + abs(y) <= N and (x + y) % 2 == N % 2:
    print("Yes")
else:
    print("No")
