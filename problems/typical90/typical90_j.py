N = int(input())
c1 = [0]
c2 = [0]
for i in range(N):
    c, s = [int(_) for _ in input().split()]
    if c == 1:
        c1.append(c1[i] + s)
        c2.append(c2[i])
    else:
        c1.append(c1[i])
        c2.append(c2[i] + s)
q = int(input())
for i in range(q):
    l, r = [int(_) for _ in input().split()]
    print(c1[r] - c1[l - 1], c2[r] - c2[l - 1])
