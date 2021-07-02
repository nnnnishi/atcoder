L, R = list(map(int, input().split()))
# 最小公約数
import math


# エラトステネスの篩
# 1はじまりにする、0と1はFalse、Nsまでの配列をつくる
def era(N):
    N += 1
    is_prime = [False, False] + [True] * (N - 2)
    for n in range(2, N):
        if is_prime[n]:
            check = n + n
            while check < N:
                is_prime[check] = False
                check += n
    return is_prime


# 素因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


A = []
pr_list = era(R)
for i in range(L, R + 1):
    if not pr_list[i]:
        A.append(i)
print(len(A))
ans = 0
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        print(A[j] // A[i])
        if A[i] != c and A[j] != c and c != 1:
            ans += 2
print(ans)