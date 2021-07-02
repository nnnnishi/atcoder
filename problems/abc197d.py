import numpy as np

N = int(input())
x0, y0 = list(map(int, input().split()))
x1, y1 = list(map(int, input().split()))

x = (x0 + x1) / 2
y = (y0 + y1) / 2


def rotation_o(u, t, deg=False):

    # 度数単位の角度をラジアンに変換
    if deg == True:
        t = np.deg2rad(t)

    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

    return np.dot(R, u)


# ベクトルの初期値
Ru = (x0 - x, y0 - y)

# 単位ベクトルに繰り返し回転行列を作用させる
Ru = rotation_o(Ru, np.pi / (N // 2))
R = Ru + (x, y)
print(R[0], R[1])
