N, M = list(map(int, input().split()))
maxnum = M // N

for i in range(maxnum, 0, -1):
    if M % i == 0:
        exit(print(i))
