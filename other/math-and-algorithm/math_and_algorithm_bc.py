N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
s = sum(A)
if s <= K and s % 2 == K % 2:
    print("Yes")
else:
    print("No")
