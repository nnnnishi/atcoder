N, K = [int(_) for _ in input().split()]
ans = 0
for i in range(1, N + 1):
    if i >= K:
        ans += 1 / N
    else:
        j = 1
        while i * (2 ** j) < K:
            j += 1
        else:
            ans += (1 / N) * (1 / 2 ** j)
print(ans)