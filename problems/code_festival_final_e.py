N = int(input())
a = [int(_) for _ in input().split()]
b = [0]
for i in range(N - 1):
    if a[i + 1] - a[i] > 0:
        b.append(1)
    elif a[i + 1] - a[i] < 0:
        b.append(-1)
# print(b)
c = 0
for i in range(len(b) - 1):
    if b[i + 1] != b[i]:
        c += 1
if c < 2:
    print(0)
else:
    print(c + 1)
