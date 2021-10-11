N = int(input())
a = [int(_) for _ in input().split()]
sa = sum(a)
if sa % N != 0:
    exit(print(-1))
else:
    t = sa // N

c = 0
d = 1
ans = 0
for i in range(N):
    c += a[i]
    # print(c, d)
    if c % d != 0 or c // d != t:
        ans += 1
        d += 1
    else:
        c = 0
        d = 1
        # print("*", i)

print(ans)
