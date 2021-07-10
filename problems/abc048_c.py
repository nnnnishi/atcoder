N, x = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
suma = [a[0]]
for i in range(N - 1):
    suma.append(a[i] + a[i + 1])
ans = 0
for i in range(N):
    if suma[i] >= x:
        c = suma[i] - x
        ans += c
        if i < N - 1:
            suma[i + 1] -= c

print(ans)