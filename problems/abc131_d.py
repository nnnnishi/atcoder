N = int(input())
t = []
for i in range(N):
    x, y = [int(_) for _ in input().split()]
    t.append([y, x])

t.sort()

c = 0
for ti in t:
    d = ti[0]
    ci = ti[1]
    if c + ci > d:
        exit(print("No"))
    else:
        c += ci
print("Yes")
