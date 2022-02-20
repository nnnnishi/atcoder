N = int(input())
d = []
diff = 0
for i in range(N):
    a, b = [int(_) for _ in input().split()]
    diff -= a
    d.append(2 * a + b)
d.sort(reverse=True)
for i in range(N):
    if diff + d[i] > 0:
        print(i + 1)
        exit()
    else:
        diff += d[i]
