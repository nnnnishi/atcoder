N = int(input())
M = 10 ** 9 + 7
print(((pow(4, N + 1, M) - 1) % M) * pow(3, -1, M) % M)

