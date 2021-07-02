N = int(input())

# エラトステネスの篩
# 1はじまりにする、0と1はFalse、N-1までの配列をつくる
is_prime = [False, False] + [True] * (N - 1)
for n in range(2, N + 1):
    if is_prime[n]:
        check = n + n
        while check <= N:
            is_prime[check] = False
            check += n

div = []
for i in range(0, N + 1):
    if is_prime[i]:
        cnt = 0
        for j in range(2, N + 1):
            while j >= i and j % i == 0:
                cnt += 1
                j = j // i
        if cnt > 0:
            div.append(cnt)

ans = 1
for d in div:
    ans *= d + 1
    ans %= 10 ** 9 + 7
print(ans)
