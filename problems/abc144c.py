N = int(input())
tmp = 10 ** 20
tmp_i = 1
for i in range(1, 10 ** 6 + 1):
    if i ** 2 > N:
        break
    if N % i == 0:
        if abs((N // i) - i) <= tmp:
            tmp = abs((N // i) - i)
            tmp_i = i
print(N // tmp_i + tmp_i - 2)
