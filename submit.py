# ユークリッド距離
import numpy

x1 = 2
y1 = 2
x2 = 4
y2 = 6
a = numpy.array([x1, y1])
b = numpy.array([x2, y2])
u = b - a
numpy.linalg.norm(u)


# 座標圧縮
def compress(arr):
    (*XS,) = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}
