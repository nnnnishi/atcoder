N = int(input())
a = list(map(int, input().split()))
X = int(input())

asum = sum(a)
c = X // asum
d = X % asum
ans = c * N

if d == 0:
    # ぴったり
    print(ans + 1)
else:
    for i in range(N):
        if d < a[i]:
            exit(print(ans + 1))
        else:
            d -= a[i]
            ans += 1

