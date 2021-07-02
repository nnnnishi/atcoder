X = [int(_) for _ in input().split()]
X.sort()

ans = 0
if (X[2] - X[1]) % 2 == 0:
    ans += (X[2] - X[1]) // 2
    if (X[2] - X[0]) % 2 == 0:
        ans += (X[2] - X[0]) // 2
    else:
        ans += (X[2] - X[0]) // 2 + 2
else:
    ans += (X[2] - X[1]) // 2
    if (X[2] - X[0]) % 2 == 0:
        ans += (X[2] - X[0]) // 2 + 2
    else:
        ans += (X[2] - X[0]) // 2 + 1
print(ans)