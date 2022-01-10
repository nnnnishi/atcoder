N, K = [int(_) for _ in input().split()]
y = 0
for i in range(1, N + 1):
    for b in range(max(1, i - (K - 1)), min(N, i + K - 1) + 1):
        for c in range(max(1, i - (K - 1)), min(N, i + K - 1) + 1):
            if abs(b - c) < K:
                y += 1

print(N ** 3 - y)
