import numpy as np


def n_shinsu(n, i, j):
    """
    nをi進数からj進数へ変換
    """
    # 11進数以上の数字を大文字そのまま
    # return np.base_repr(int(str(n), i), base=j)
    # 小文字にする
    return str.lower(np.base_repr(int(str(n), i), base=j))


K = int(input())
a, b = [int(_) for _ in input().split()]
print(int(n_shinsu(a, K, 10)) * int(n_shinsu(b, K, 10)))

