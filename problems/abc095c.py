A, B, C, X, Y = [int(_) for _ in input().split()]
ans = 10 ** 10
for i in range(max(X + 1, Y + 1)):
    ans = min(ans, max((X - i) * A, 0) + max((Y - i) * B, 0) + 2 * C * i)
print(ans)