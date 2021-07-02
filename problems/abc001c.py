Deg, Dis = [int(_) for _ in input().split()]
W = 0


def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p


Dis = my_round(Dis / 60, 1)

if 0 <= Dis <= 0.2:
    W = 0
elif 0.3 <= Dis <= 1.5:
    W = 1
elif 1.6 <= Dis <= 3.3:
    W = 2
elif 3.4 <= Dis <= 5.4:
    W = 3
elif 5.5 <= Dis <= 7.9:
    W = 4
elif 8.0 <= Dis <= 10.7:
    W = 5
elif 10.8 <= Dis <= 13.8:
    W = 6
elif 13.9 <= Dis <= 17.1:
    W = 7
elif 17.2 <= Dis <= 20.7:
    W = 8
elif 20.8 <= Dis <= 24.4:
    W = 9
elif 24.5 <= Dis <= 28.4:
    W = 10
elif 28.5 <= Dis <= 32.6:
    W = 11
elif 32.7 <= Dis:
    W = 12

D = "N"
if W == 0:
    exit(print("C", 0))
else:
    if 112.5 <= Deg < 337.5:
        D = "NNE"
    elif 337.5 <= Deg < 562.5:
        D = "NE"
    elif 562.5 <= Deg < 787.5:
        D = "ENE"
    elif 787.5 <= Deg < 1012.5:
        D = "E"
    elif 1012.5 <= Deg < 1237.5:
        D = "ESE"
    elif 1237.5 <= Deg < 1462.5:
        D = "SE"
    elif 1462.5 <= Deg < 1687.5:
        D = "SSE"
    elif 1687.5 <= Deg < 1912.5:
        D = "S"
    elif 1912.5 <= Deg < 2137.5:
        D = "SSW"
    elif 2137.5 <= Deg < 2362.5:
        D = "SW"
    elif 2362.5 <= Deg < 2587.5:
        D = "WSW"
    elif 2587.5 <= Deg < 2812.5:
        D = "W"
    elif 2812.5 <= Deg < 3037.5:
        D = "WNW"
    elif 3037.5 <= Deg < 3262.5:
        D = "NW"
    elif 3262.5 <= Deg < 3487.5:
        D = "NNW"
print(D, W)
