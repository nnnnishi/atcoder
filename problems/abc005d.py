from itertools import accumulate, product, permutations, combinations
from collections import Counter, deque, defaultdict

N = int(input())
D = []
Dsum = []
for i in range(N):
    D.append([int(_) for _ in input().split()])
# 累積和を求める
for d in D:
    Dsum.append([0] + list(accumulate(d)))

dic = defaultdict(int)
# 左上と右下の座標を選ぶ
for i1 in range(N ** 2):
    for i2 in range(i1, N ** 2):
        # 何個の長方形か数える
        x1 = i1 % N
        y1 = i1 // N
        x2 = i2 % N
        y2 = i2 // N
        n = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        # 長方形領域の和を求める
        c = 0
        for y in range(y1, y2 + 1):
            if x2 > x1:
                c += Dsum[y][x2 + 1] - Dsum[y][x1]
            else:
                c += Dsum[y][x1 + 1] - Dsum[y][x2]
        if c >= dic[n]:
            dic[n] = c

for i in range(N ** 2 - 1):
    if dic[i + 1] < dic[i]:
        dic[i + 1] = dic[i]
Q = int(input())
for i in range(Q):
    print(dic[int(input())])
