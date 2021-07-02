from itertools import accumulate, product, permutations, combinations

N = int(input())
A = [0] * (1000001 + 1)
for _ in range(N):
    a, b = [int(_) for _ in input().split()]
    A[a] += 1
    A[b + 1] -= 1
sumA = list(accumulate(A))
ans = 0
tmp = 0
print(max(sumA))
