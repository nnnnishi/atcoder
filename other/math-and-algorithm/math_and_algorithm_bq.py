N = int(input())
M = 10 ** 9 + 7
a = ((1 + N) * N // 2) % M
print(a * a % M)

