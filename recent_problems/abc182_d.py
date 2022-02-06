N = int(input())
A = [int(_) for _ in input().split()]
ans = 0
tmp = 0
cummax = 0
cumA = [0] * N
cumA[0] = A[0]
for i in range(1, N):
    cumA[i] = A[i] + cumA[i - 1]
for i in range(N):
    if cumA[i] > cummax:
        cummax = cumA[i]
        tmp += cumA[i]
        if tmp > ans:
            ans = tmp
    else:
        if tmp + cummax > ans:
            ans = tmp + cummax
        tmp += cumA[i]
print(ans)
