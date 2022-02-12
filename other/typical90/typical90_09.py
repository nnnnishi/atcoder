# https://atcoder.jp/contests/typical90/tasks/typical90_i
# https://enakai00.hatenablog.com/entry/2021/07/31/220024
import math


def dist(j, k, mod):
    return (k - j) % mod


def undist(j, k, mod):
    return (k + j) % mod


def deg_normal(deg):
    if deg < 0:
        deg += 360
    if deg > 180:
        deg = 360 - deg
    return deg


N = int(input())
p = []

for _ in range(N):
    p.append([int(_) for _ in input().split()])


result = 0
for i in range(N):  # O(N)
    O = p[i]  # 原点
    deg_list = []
    # 点iを原点Oとした偏角の昇順リストを作成する
    for j in range(N):  # O(N)
        if j == i:
            continue
        x = p[j][0] - O[0]
        y = p[j][1] - O[1]
        # (x, y)とx-axisの角度を求める
        # arctan(y/x)は90度で発散するのでcosで符号を調整
        cos = x / math.sqrt(x * x + y * y)
        # 度数deg
        deg = math.degrees(math.acos(cos))
        if y < 0:
            deg += (180 - deg) * 2
        deg_list.append(deg)
    deg_list.sort()  # O(N*log N)

    for j in range(len(deg_list)):  # O(N)
        mod = len(deg_list)
        # jの角度を中心として、j+1をlow、j-1をhighとし間を狭めていく
        high = -1  # j - 1
        low = j + 1
        # jを基準として何番目か
        high = dist(j, high, mod)
        low = dist(j, low, mod)
        while high > low:  # O(log N)
            m = low + (high - low) // 2
            # j基準から元の基準に戻す
            deg = deg_list[undist(j, m, mod)] - deg_list[j]
            deg_r = deg_list[undist(j, m + 1, mod)] - deg_list[j]
            deg = deg_normal(deg)
            deg_r = deg_normal(deg_r)
            # 中央より大きい側なら小さい側を中央に
            if deg_r > deg:
                low = m + 1
            # 中央より小さい側なら大きい側を中央に
            else:
                high = m
        # 一致したらjとの角度を出す
        max_deg = deg_list[undist(j, low, mod)] - deg_list[j]
        # 0~360度へ変換
        max_deg = deg_normal(max_deg)
        if max_deg > result:
            result = max_deg

print(result)
