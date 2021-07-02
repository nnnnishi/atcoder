Q = int(input())
LR = []
for i in range(Q):
    l, r = [int(_) for _ in input().split()]
    LR.append([l, r])
# 1 ~ 10**5が素数かどうか確認
P = [False] * (10 ** 5 + 1)
for i in range(2, 10 ** 5 + 1):
    prime = True
    for j in range(2, i):
        if (j ** 2) > i:
            break
        if i % j == 0:
            prime = False
            break
    if prime:
        P[i] = True
# 1 ~ 10**5がlike a numberかどうか確認
LN = [0] * (10 ** 5 + 1)
for i in range(10 ** 5 + 1):
    if P[i] and P[(i + 1) // 2]:
        LN[i] = 1
# 累積和
sumLN = [0]
for i in range(1, 10 ** 5 + 1):
    sumLN.append(sumLN[i - 1] + LN[i])
for l, r in LR:
    print(sumLN[r] - sumLN[l - 1])
