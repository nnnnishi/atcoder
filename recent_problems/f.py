N, K = list(map(int, input().split()))
ans = 0

for b in range(K + 1, N + 1):
    ans += (b - K) * (N // b)
    if K > 0:
        if (N % b) >= K:
            ans += (N % b) - K + 1
    else:
        ans += N % b
print(ans)
