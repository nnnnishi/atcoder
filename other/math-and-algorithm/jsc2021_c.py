A, B = [int(_) for _ in input().split()]
ans = 1
for g in range(2, B):
    if (B // g) - (-(-A // g)) > 0:
        ans = g
print(ans)
