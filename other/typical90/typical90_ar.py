N, Q = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
idx = [i for i in range(N)]
s = 0

for i in range(Q):
    t, x, y = [int(_) for _ in input().split()]
    if t == 1:
        tmp = idx[(x - 1 - s) % N]
        idx[(x - 1 - s) % N] = idx[(y - 1 - s) % N]
        idx[(y - 1 - s) % N] = tmp
    elif t == 2:
        s += 1
    else:
        print(A[idx[((x - 1 - s)) % N]])
