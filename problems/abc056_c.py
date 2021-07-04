N = int(input())
c = 0
for t in range(1, N + 1):
    c += t
    if c >= N:
        exit(print(t))
