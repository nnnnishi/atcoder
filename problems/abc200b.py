N, K = list(map(int, input().split()))
for i in range(K):
    if N % 200 == 0:
        N = N // 200
    else:
        N = int(str(N) + str(200))
print(N)