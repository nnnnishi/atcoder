# エラトステネスの篩
# O(NloglogN)
N = int(input())

# 0はじまり、Nまで
is_prime = [False, False] + [True] * (N - 1)
for n in range(2, N + 1):
    if is_prime[n]:
        check = n + n
        while check < N + 1:
            is_prime[check] = False
            check += n

p = []
for i, x in enumerate(is_prime):
    if x:
        p.append(i)
print(*p)
