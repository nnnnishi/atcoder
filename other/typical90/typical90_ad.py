# エラトステネスの篩
# O(NloglogN)
N, K = [int(_) for _ in input().split()]

# 0はじまり、N-1まで
is_prime = [0, 0] + [0] * (N - 1)
for n in range(2, N):
    if is_prime[n] == 0:
        is_prime[n] = 1
        check = n + n
        while check <= N:
            is_prime[check] += 1
            check += n
# print(is_prime)
cnt = 0
for x in is_prime:
    if x >= K:
        cnt += 1
print(cnt)