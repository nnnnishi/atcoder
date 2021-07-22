import numpy as np

N = 300

# 10 -> 2進数
print(str(format(N, "b")))
# 10 -> 8進数
print(str(format(N, "o")))
# 10 -> 16進数
print(format(N, "x"))


def n_shinsu(n, i, j):
    """
    nをi進数からj進数へ変換
    """
    # 11進数以上の数字を大文字そのまま
    # return np.base_repr(int(str(n), i), base=j)
    # 小文字にする
    return str.lower(np.base_repr(int(str(n), i), base=j))


# 文字型になっている
print(n_shinsu(N, 10, 2))
print(n_shinsu(N, 10, 8))
print(n_shinsu(N, 10, 16))
print(n_shinsu(N, 4, 10))
