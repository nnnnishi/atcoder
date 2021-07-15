N = int(input())
A = [int(_) for _ in input().split()]
A += [0]
b = 0
sumA = 0
for i in range(N + 1):
    sumA += abs(A[i] - b)
    b = A[i]
b = 0
for i in range(N):
    print(sumA - abs(A[i] - b) - abs(A[i + 1] - A[i]) + abs(A[i + 1] - b))
    b = A[i]
