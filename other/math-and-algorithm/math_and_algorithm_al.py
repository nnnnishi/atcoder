T = int(input())
N = int(input())
A = [0] * (T + 1)
for i in range(N):
    l, r = [int(_) for _ in input().split()]
    A[l] += 1
    A[r] -= 1

for i in range(1, T):
    A[i] += A[i - 1]

for i in range(T):
    print(A[i])
