N, K = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
idx = 0
for i in range(N):
    if a[i] == 1:
        idx = i
        break
if N == K:
    exit(print(1))

print(1 + -(-(N - K) // (K - 1)))
