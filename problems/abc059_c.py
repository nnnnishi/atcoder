N = int(input())
a = [int(_) for _ in input().split()]

suma = [0] * N
suma[0] = a[0]
for i in range(1, N):
    suma[i] = a[i] + suma[i - 1]
# print(suma)
fans = 10 ** 20
for pos in [1, 0]:
    suma = [0] * N
    suma[0] = a[0]
    for i in range(1, N):
        suma[i] = a[i] + suma[i - 1]
    sousa = 0
    ans = 0
    for i in range(N):
        suma[i] += sousa
        # 前がpos
        if pos:
            if suma[i] >= 0:
                # -1にする
                ans += suma[i] + 1
                sousa -= suma[i] + 1
        else:
            if suma[i] <= 0:
                # 1にする
                ans += 1 - suma[i]
                sousa += 1 - suma[i]
        pos = (pos + 1) % 2
    fans = min(ans, fans)
print(fans)