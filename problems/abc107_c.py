N, K = [int(_) for _ in input().split()]
x = [int(_) for _ in input().split()]

ans = 10 ** 10
for i in range(N - K + 1):
    if x[i] <= 0 <= x[i + K - 1]:
        ans = min(ans, x[i + K - 1] - x[i] + min(abs(x[i + K - 1]), abs(x[i])))
    elif 0 > x[i + K - 1]:
        ans = min(ans, x[i + K - 1] - x[i] + abs(x[i + K - 1]))
    elif x[i] > 0:
        ans = min(ans, x[i + K - 1] - x[i] + abs(x[i]))

print(ans)