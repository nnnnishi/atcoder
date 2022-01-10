# 多角形に点が包含されるか
# Ray Casting Algorithm
# 点w から半直線を出し、多角形Pと何回交差するかで包含判定する。
# 多角形P と奇数回交差している場合に包含されていると判定する。
# 計算量: O(N)
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bu
# https://tjkendev.github.io/procon-library/python/geometry/point_inside_polygon.html
# https://github.com/E869120/math-algorithm-book/blob/main/editorial/chap6-21_25/chap6-21_25.pdf

import sys

input = sys.stdin.readline
# 内積計算

# Ray casting algorithm
def inside_polygon(p0, qs):
    """
    p0: 判定する点C (x,y)=(A,B)
    qs: 多角形の頂点のリスト, 隣り合う点どうしが連続するリストとして持つ
    """
    cnt = 0
    L = len(qs)
    A, B = p0
    for i in range(L):
        xa, ya = qs[i - 1][0] - A, qs[i - 1][1] - B
        xb, yb = qs[i][0] - A, qs[i][1] - B
        # 上下をあわせる
        if ya > yb:
            xa, xb = xb, xa
            ya, yb = yb, ya
        # 内積
        cv = xa * xb + ya * yb
        # 外積
        sv = xa * yb - xb * ya
        # 外積が0で内積が0以下ならば線上に点があるので内側に判定
        if sv == 0 and cv <= 0:
            return True
        # Cからx軸と平行にAB方向に伸ばした半直線がABが交差するかどうか
        # y軸上の間,　(xa,ya) (A,B) (xb,yb) の順で反時計回りになっている
        if ya <= 0 < yb and sv < 0:
            cnt += 1
    return cnt % 2 == 1


N = int(input())
L = []
for _ in range(N):
    L.append([int(_) for _ in input().split()])
X, Y = [int(_) for _ in input().split()]

if inside_polygon([X, Y], L):
    print("INSIDE")
else:
    print("OUTSIDE")

