N = int(input())
A = []
A.append([int(_) for _ in input().split()])
A.append([int(_) for _ in input().split()])

# 分岐
ans = 0
for i in range(N):
    tmp = 0
    for j in range(i + 1):
        tmp += A[0][j]
    for k in range(i, N):
        tmp += A[1][k]
    ans = max(tmp, ans)
print(ans)