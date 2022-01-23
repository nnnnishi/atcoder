ans = 0
N, X = [int(_) for _ in input().split()]
for a in range(1, N + 1):
    for b in range(a + 1, N + 1):
        for c in range(b + 1, N + 1):
            if a + b + c == X:
                ans += 1

print(ans)
