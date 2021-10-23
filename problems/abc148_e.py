N = int(input())
if N % 2 != 0:
    print(0)
else:
    k = N // 2
    f = 0
    for i in range(1, 30):
        f += k // pow(5, i)
    print(f)
