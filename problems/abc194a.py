N = int(input())
A = []
B = []
for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)
ans = 10 ** 6
for i in range(N):
    for j in range(N):
        if i == j:
            tmp = A[i] + B[j]
        else:
            tmp = max(A[i], B[j])
        ans = min(tmp, ans)
print(ans)