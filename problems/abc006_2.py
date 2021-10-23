N = int(input())
a = [0, 0, 1]
M = 10007
for i in range(3, N + 1):
    x = a[i - 3] + a[i - 2] + a[-1]
    x %= M
    a.append(x)
print(a[N - 1])
