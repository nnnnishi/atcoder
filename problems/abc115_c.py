N, K = [int(_) for _ in input().split()]
h = []
for i in range(N):
    h.append(int(input()))
h.sort()
ans = 10 ** 10
for i in range(N - K + 1):
    ans = min(ans, abs(h[i] - h[i + K - 1]))
print(ans)
