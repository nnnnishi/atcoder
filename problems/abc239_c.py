x1, y1, x2, y2 = list(map(int, input().split()))


def move(x, y):
    ml = []
    for dx, dy in [
        [1, 2],
        [2, 1],
        [2, -1],
        [1, -2],
        [-1, 2],
        [-2, 1],
        [-2, -1],
        [-1, -2],
    ]:
        ml.append([x + dx, y + dy])
    return ml


cand1 = move(x1, y1)
cand2 = move(x2, y2)

for x3, y3 in cand1:
    if [x3, y3] in cand2:
        print("Yes")
        exit()
print("No")

