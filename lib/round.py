# 四捨五入
def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p


d = 0.5
print(my_round(d, 0))
print(round(d, 0))