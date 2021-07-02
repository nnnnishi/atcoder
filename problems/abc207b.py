a, b, c, d = list(map(int, input().split()))
if c * d - b <= 0:
    print(-1)
else:
    print(-(-1 * a // (c * d - b)))
