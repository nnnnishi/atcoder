N, P = list(map(int, input().split()))
a = (P - 1) * pow(P - 2, N - 1, 10 ** 9 + 7)
a = a % (10 ** 9 + 7)
print(a)