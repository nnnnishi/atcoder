# rotation
import numpy as np


def rotation_o(u, t, deg=False):
    # 度数単位の角度をラジアンに変換
    if deg == True:
        t = np.deg2rad(t)

    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

    return np.dot(R, u)


print(rotation_o([1, 0], 90, True))
print(rotation_o([1, 0], 45, True))
print(rotation_o([1, 0], np.pi / 2))
