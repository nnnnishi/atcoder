N = int(input())
a = []
b = []
c = []
for _ in range(N):
    a1, b1, c1 = list(map(int, input().split()))
    a.append(a1)
    b.append(b1)
    c.append(c1)

happy = [[0, 0, 0]]
n = 0
for ai, bi, ci in zip(a, b, c):
    n += 1
    happy.append([0, 0, 0])
    if n == 1:
        happy[1][0] = ai
        happy[1][1] = bi
        happy[1][2] = ci
    if n >= 2:
        happy[n][0] = max(happy[n - 1][1] + ai, happy[n - 1][2] + ai)
        happy[n][1] = max(happy[n - 1][0] + bi, happy[n - 1][2] + bi)
        happy[n][2] = max(happy[n - 1][0] + ci, happy[n - 1][1] + ci)

print(max(happy[N]))