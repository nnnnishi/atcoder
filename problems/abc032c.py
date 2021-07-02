from itertools import accumulate, product, permutations, combinations

N, Q = [int(_) for _ in input().split()]

A = [0] * (N + 1)
for _ in range(Q):
    l, r = [int(_) for _ in input().split()]
    A[l - 1] += 1
    A[r] -= 1
sumA = list(accumulate(A))
for i in range(N):
    if sumA[i] % 2 == 0:
        sumA[i] = "0"
    else:
        sumA[i] = "1"
print("".join(sumA[:N]))