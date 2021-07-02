N = int(input())
ans = 0
for K in range(1, N):
    ans += N / (N - K)
print(ans)
