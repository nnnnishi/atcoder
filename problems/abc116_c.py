N = int(input())
A = [int(_) for _ in input().split()]
cnt = 0
for i in range(N):
    if A[i] != 0:
        cnt += A[i]
        t = A[i]
        A[i] = 0
        for j in range(i + 1, N):
            if A[j] >= t:
                A[j] -= t
            else:
                t = A[j]
                A[j] = 0
    # print(A)
print(cnt)