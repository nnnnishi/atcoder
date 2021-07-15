K, N = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
L = [A[0] + (K - A[N - 1])]
for i in range(N - 1):
    L.append(A[i + 1] - A[i])
print(K - max(L))
