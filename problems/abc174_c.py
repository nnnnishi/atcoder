N = int(input())
check = set()
n = 7
n = n % N
if n == 0:
    exit(print(1))
i = 1
while n not in check:
    check.add(n)
    n = (n + 7 * pow(10, i, N)) % N
    i += 1
    if n == 0:
        exit(print(i))
print(-1)