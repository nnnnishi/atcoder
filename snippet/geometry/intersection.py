# 外積計算
def cross(ax, ay, bx, by):
    return ax * by - bx * ay


# 入力
XA, YA = map(int, input().split())
XB, YB = map(int, input().split())
XC, YC = map(int, input().split())
XD, YD = map(int, input().split())

crossABAC = cross(XB - XA, YB - YA, XC - XA, YC - YA)
crossABAD = cross(XB - XA, YB - YA, XD - XA, YD - YA)
crossCDCA = cross(XD - XC, YD - YC, XA - XC, YA - YC)
crossCDCB = cross(XD - XC, YD - YC, XB - XC, YB - YC)

# 全て一直線上に並ぶ
if crossABAC == 0 and crossABAD == 0:
    # 重なる部分がある
    maxAB = max([XA, YA], [XB, YB])
    minAB = min([XA, YA], [XB, YB])
    maxCD = max([XC, YC], [XD, YD])
    minCD = min([XC, YC], [XD, YD])
    if max(minAB, minCD) <= min(maxAB, maxCD):
        print("Yes")
    else:
        print("No")
# すべて一直線上ではない
else:
    if crossABAC * crossABAD <= 0 and crossCDCA * crossCDCB <= 0:
        print("Yes")
    else:
        print("No")

