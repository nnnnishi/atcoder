N, K = list(map(int, input().split()))
R = 5000
A = [[0] * (R + 1) for _ in range(R + 1)]
for i in range(N):
    a, b = [int(_) for _ in input().split()]
    A[a][b] += 1
sumA = [[0] * (R + 1) for _ in range(R + 1)]
ans = 0
# (0,0), (0,y), (x,0), (x,y) の矩形で累積和
for y in range(1, R + 1):
    for x in range(1, R + 1):
        sumA[y][x] = A[y][x] + sumA[y - 1][x] + sumA[y][x - 1] - sumA[y - 1][x - 1]
# (x1-K,y1-K), (x1,y1-K), (x1-K,y1), (x1,y1) の矩形で累積和
K = K + 1
for y1 in range(K, R + 1):
    for x1 in range(K, R + 1):
        cnt = sumA[y1][x1] - sumA[y1 - K][x1] - sumA[y1][x1 - K] + sumA[y1 - K][x1 - K]
        ans = max(cnt, ans)
# print(A)
# print(sumA)
print(ans)
