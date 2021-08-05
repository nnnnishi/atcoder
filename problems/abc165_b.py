X = int(input())
c = 100
for i in range(1, 10 ** 7):
    c = c + c // 100
    if c >= X:
        exit(print(i))