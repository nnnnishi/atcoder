# rotation
import numpy as np

A, B, H, M = [int(_) for _ in input().split()]


def rotation_o(u, t, deg=False):
    # 度数単位の角度をラジアンに変換
    if deg == True:
        t = np.deg2rad(t)
    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    return np.dot(R, u)


long = rotation_o([0, A], H * (360 // 12) + M * (30 / 60), True)
short = rotation_o([0, B], M * (360 // 60), True)
print(np.sqrt((long[0] - short[0]) ** 2 + (long[1] - short[1]) ** 2))
