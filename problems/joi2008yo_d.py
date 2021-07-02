N = int(input())
A = []
for i in range(N):
    A.append(tuple(map(int, input().split())))
M = int(input())
B = []
for i in range(M):
    B.append(tuple(map(int, input().split())))
Bset = set(B)

for a in A:
    for b in B:
        vec_x = b[0] - a[0]
        vec_y = b[1] - a[1]
        ok = True
        for a2 in A:
            if (a2[0] + vec_x, a2[1] + vec_y) not in Bset:
                ok = False
                break
        if ok:
            exit(print(vec_x, vec_y))
