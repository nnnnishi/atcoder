N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
a = []
for i in range(N):
    a.append([A[i], 1])
for i in range(M):
    a.append([B[i], 0])
a.sort()
n = a[0][0]
c = a[0][1]
ans = 10 ** 10
for i in range(1, N + M):
    if a[i][1] == c:
        n = a[i][0]
    else:
        # print(a[i])
        ans = min(ans, abs(a[i][0] - n))
        c = a[i][1]
        n = a[i][0]
# print(a)
print(ans)