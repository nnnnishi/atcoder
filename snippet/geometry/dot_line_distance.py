import math


def distance(ax, ay, bx, by, cx, cy):
    """
    線分cbと点aの距離を計算
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ae
    """
    BAx = ax - bx
    BAy = ay - by
    BCx = cx - bx
    BCy = cy - by
    CAx = ax - cx
    CAy = ay - cy
    CBx = bx - cx
    CBy = by - cy

    pattern = 2
    # BAとBCの内積が負 -> BAの距離が最短
    if BAx * BCx + BAy * BCy < 0:
        pattern = 1
    # CAとCBの内積が負 -> CAの距離が最短
    if CAx * CBx + CAy * CBy < 0:
        pattern = 3
    ans = 0
    if pattern == 1:
        ans = math.sqrt(BAx ** 2 + BAy ** 2)
    elif pattern == 3:
        ans = math.sqrt(CAx ** 2 + CAy ** 2)
    elif pattern == 2:
        # 平行四辺形の面積
        S = abs(BAx * CAy - BAy * CAx)
        BCLength = math.sqrt(BCx ** 2 + BCy ** 2)
        ans = S / BCLength
    return ans


ax, ay = [int(_) for _ in input().split()]
bx, by = [int(_) for _ in input().split()]
cx, cy = [int(_) for _ in input().split()]

print(distance(ax, ay, bx, by, cx, cy))
