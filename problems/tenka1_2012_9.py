# Nより小さい素数をエラトステネスの篩で数える
N = int(input())

# 1はじまりにする、0と1はFalse、N-1までの配列をつくる
is_prime = [False, False] + [True] * (N - 2)
for n in range(2, N):
    if is_prime[n]:
        check = n + n
        while check < N:
            is_prime[check] = False
            check += n

# Trueの数を数える
print(sum([1 for i in range(len(is_prime)) if is_prime[i]]))