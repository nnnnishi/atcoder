N = int(input())
ans = 0
for i in range(1000):
    if 2 ** i <= N:
        ans = i
    else:
        exit(print(ans))
