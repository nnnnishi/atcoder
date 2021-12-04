# 四捨五入
def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p


print(int(my_round(float(input()), 0)))

