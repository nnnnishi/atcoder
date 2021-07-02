N, K = [int(_) for _ in input().split()]
A = []
for i in range(N):
    A.append([int(_) for _ in input().split()])
A.sort()
cnt = 0
for a in A:
    cnt += a[1]
    if cnt >= K:
        exit(print(a[0]))