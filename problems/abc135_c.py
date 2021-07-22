N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

ans = 0
for i in range(N):
    if A[i] <= B[i]:
        ans += A[i]
        B[i] -= A[i]
        A[i] = 0
        if A[i + 1] <= B[i]:
            ans += A[i + 1]
            B[i] -= A[i + 1]
            A[i + 1] = 0
        else:
            ans += B[i]
            A[i + 1] -= B[i]
            B[i] = 0
    else:
        ans += B[i]
        A[i] -= B[i]
        B[i] = 0
print(ans)