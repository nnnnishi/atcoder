# X以上の素数のうち最小のもの
X = int(input())
# 大きめな数
INF = 10 ** 6
is_prime = [False, False] + [True] * INF
for n in range(2, INF + 2):
    if is_prime[n]:
        if n >= X:
            exit(print(n))
        check = n + n
        while check < INF:
            is_prime[check] = False
            check += n
