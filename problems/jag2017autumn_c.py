import math

l, r = [int(_) for _ in input().split()]

N = int(math.sqrt(r)) + 1

# エラトステネスの篩
# 1はじまりにする、0と1はFalse、N-1までの配列をつくる
L = 10 ** 5
is_prime = [False, False] + [True] * (L - 2)
for n in range(2, L):
    if is_prime[n]:
        check = n + n
        while check < L:
            is_prime[check] = False
            check += n

val = []
cnt = []
for i in range(l, r + 1):
    val.append(i)
    cnt.append(0)

for i in range(N):
    if is_prime[i]:
        t = i
        c = 1
        # l以降の最初のtの倍数
        while t ** c <= r:
            if l % (t ** c) == 0:
                k = l // (t ** c)
            else:
                k = l // (t ** c) + 1
            s = k * (t ** c)
            while s <= r:
                cnt[s - l] += 1
                val[s - l] = val[s - l] // t
                s += t ** c
            c += 1
ans = 0
# print(cnt)
# print(val)
for j in range(len(val)):
    if val[j] != 1:
        cnt[j] += 1
    if is_prime[cnt[j]]:
        ans += 1

print(ans)