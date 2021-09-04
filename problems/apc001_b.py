N = int(input())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
sa = sum(a)
sb = sum(b)
minA = 0
minB = 0
c = sb - sa

if c < 0:
    exit(print("No"))
for i in range(N):
    if a[i] - b[i] >= 0:
        minB += a[i] - b[i]
    else:
        # minA += -(-(b[i] - a[i]) // 2)
        minA += (b[i] - a[i]) // 2

if minA >= minB:
    print("Yes")
else:
    print("No")
