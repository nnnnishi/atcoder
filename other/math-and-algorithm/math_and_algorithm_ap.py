N = int(input())
d = [0] * N
d[0] = 1
d[1] = 1
MOD = 10 ** 9 + 7
for i in range(2, N):
    d[i] = (d[i - 1] + d[i - 2]) % MOD
print(d[N - 1])
