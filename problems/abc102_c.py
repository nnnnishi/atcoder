N = int(input())
A = [int(_) for _ in input().split()]
L = []
for i in range(N):
    L.append(A[i] - (i + 1))
L.sort()

if N % 2 != 0:
    b = L[N // 2]
else:
    b = min(L[N // 2], L[N // 2 - 1])

c = 0
for i in range(N):
    c += abs(A[i] - (b + i + 1))
print(c)