P = float(input())


def func(x):
    return x + (P / (2 ** (x / 1.5)))


left = 0
right = 100
while abs(right - left) > 10e-9:
    mid_r = (right * 2 / 3) + (left / 3)
    mid_l = (right / 3) + (left * 2 / 3)
    rf = func(mid_r)
    lf = func(mid_l)
    if rf >= lf:
        right = mid_r
    else:
        left = mid_l
print(func(right))