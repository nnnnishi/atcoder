N, M = [int(_) for _ in input().split()]
X = [int(_) for _ in input().split()]
if M <= N:
    print(0)
else:
    X.sort()
    ans = 0
    diff = []
    for i in range(M - 1):
        ans += X[i + 1] - X[i]
        diff.append(X[i + 1] - X[i])
    diff.sort(reverse=True)

    for i in range(N - 1):
        ans -= diff[i]
    print(ans)