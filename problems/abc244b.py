N = int(input())
S = input()
x, y = 0, 0

d = [[1, 0], [0, -1], [-1, 0], [0, 1]]
idx = 0
for i in range(N):
    if S[i] == "S":
        dx, dy = d[idx]
        x += dx
        y += dy
    else:
        idx += 1
        idx %= 4
print(x, y)
