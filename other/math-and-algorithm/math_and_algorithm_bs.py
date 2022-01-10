N = int(input())
ans = 10 ** 30
if N == 1:
    print(4)
    exit()
for x in range(1, N):
    if x ** 2 > N:
        break
    if N % x == 0:
        y = N // x
        if ans > 2 * (x + y):
            ans = 2 * (x + y)
print(ans)
