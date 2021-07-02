# 再帰用
N = int(input())
ans = 10 ** 10
upper = N
for i in range(1, N + 1):
    if N % i == 0:
        tmp = max(len(str(i)), len(str(N // i)))
        ans = min(ans, tmp)
        upper = N // i
    if i ** 2 > N:
        break
    if i >= upper:
        break
print(ans)
