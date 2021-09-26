N, X = [int(_) for _ in input().split()]

a = [1]
p = [1]
for i in range(50):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)


def dp(n, x):
    if x == 0:
        return 0
    if n == 0:
        return 1
    # まんなかのpateまで
    if x <= a[n - 1] + 1:
        return dp(n - 1, x - 1)
    elif x == a[n - 1] + 2:
        return dp(n - 1, a[n - 1]) + 1
    elif x > a[n - 1] + 2:
        return dp(n - 1, x - (a[n - 1] + 2)) + p[n - 1] + 1


print(dp(N, X))

