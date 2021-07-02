N, H = [int(_) for _ in input().split()]
A, B, C, D, E = [int(_) for _ in input().split()]
H -= 0.00000001
ans = 10 ** 30
for i in range(N + 1):
    j = max(0, -(-(-H - (B + E) * i + E * N) // (D + E)))
    ans = min(ans, i * A + j * C)

print(int(ans))