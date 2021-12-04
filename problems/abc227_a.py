N, K, A = [int(_) for _ in input().split()]
A -= 1
while K > 0:
    A += 1
    K -= 1
    if A > N:
        A = 1
print(A)

