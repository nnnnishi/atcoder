import copy
from operator import itemgetter

N, Q = [int(_) for _ in input().split()]
p = []
for _ in range(N):
    x1, y1 = [int(_) for _ in input().split()]
    # 45度回転
    p.append([x1 - y1, x1 + y1])
p_copy = copy.deepcopy(p)
p.sort(key=itemgetter(0))
x_min = p[0][0]
x_max = p[-1][0]
p.sort(key=itemgetter(1))
y_min = p[0][1]
y_max = p[-1][1]


for _ in range(Q):
    q = int(input())
    q -= 1
    x = p_copy[q][0]
    y = p_copy[q][1]
    d = max(abs(x_min - x), abs(x_max - x), abs(y_min - y), abs(y_max - y))
    print(d)

