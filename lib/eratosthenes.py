# エラトステネスの篩
# O(NloglogN)
N = 10

# 0はじまり、N-1まで
is_prime = [False, False] + [True] * (N - 2)
for n in range(2, N):
    if is_prime[n]:
        check = n + n
        while check < N:
            is_prime[check] = False
            check += n

print(is_prime)
