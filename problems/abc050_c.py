N = int(input())
a = [int(_) for _ in input().split()]
a.sort()
c = [abs(N - 2 * i + 1) for i in range(1, N + 1)]
c.sort()
for i in range(N):
    if a[i] != c[i]:
        exit(print(0))
if a[0] == 0:
    print(pow(2, (N - 1) // 2, 10 ** 9 + 7))
else:
    print(pow(2, (N // 2), 10 ** 9 + 7))
