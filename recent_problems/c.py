N = int(input())

n = (N - 1) % 20
g = (N - 1) // 20
if g % 2 == 0:
    print(n + 1)
else:
    print(20 - n)
