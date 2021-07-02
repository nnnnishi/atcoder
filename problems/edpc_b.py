N, K = list(map(int, input().split()))
h = [0] + list(map(int, input().split()))
INF = 10 ** 20
cost = [INF] * (N + 1)
cost[1] = 0

for i in range(2, N + 1):
    for j in range(1, K + 1):
        if i - j >= 1:
            cost[i] = min(cost[i], cost[i - j] + abs(h[i] - h[i - j]))

print(cost[N])
