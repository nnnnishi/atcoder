N, K = [int(_) for _ in input().split()]
if K == 1:
    exit(print(N))
ans = 0
cont = 0
b = -1
for _ in range(N):
    a = int(input())
    if a > b:
        cont += 1
        if cont >= K:
            ans += 1
        b = a
    else:
        cont = 1
        b = a
print(ans)
