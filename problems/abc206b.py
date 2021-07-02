N = int(input())
check = True
d = 0
cnt = 0
while check:
    d += 1
    cnt += d
    if N <= cnt:
        exit(print(d))
