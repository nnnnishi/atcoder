from cmath import sqrt
import math

N, M = [int(_) for _ in input().split()]
fix = []
non_fix = []
for _ in range(N):
    x, y, r = [int(_) for _ in input().split()]
    fix.append([x, y, r])
if M == 0:
    ans = 1000
    for i in range(N):
        ans = min(ans, fix[i][2])
    print(ans)
    exit()
for _ in range(M):
    x, y = [int(_) for _ in input().split()]
    non_fix.append([x, y])

# 候補の長さの全列挙
setL = set()

for i in range(M):
    for j in range(i + 1, M):
        setL.add(
            math.sqrt(
                abs(non_fix[i][0] - non_fix[j][0]) ** 2
                + abs(non_fix[i][1] - non_fix[j][1]) ** 2
            )
            / 2
        )
for i in range(M):
    for j in range(N):
        setL.add(
            math.sqrt(
                abs(non_fix[i][0] - fix[j][0]) ** 2
                + abs(non_fix[i][1] - fix[j][1]) ** 2
            )
            - fix[j][2]
        )
L = list(setL)
L.sort()
# 長さansでいけるかどうかチェック
def is_ok(ans):
    for i in range(M):
        for j in range(i + 1, M):
            if (
                math.sqrt(
                    abs(non_fix[i][0] - non_fix[j][0]) ** 2
                    + abs(non_fix[i][1] - non_fix[j][1]) ** 2
                )
                < 2 * ans
            ):
                return False
    for i in range(M):
        for j in range(N):
            if (
                math.sqrt(
                    abs(non_fix[i][0] - fix[j][0]) ** 2
                    + abs(non_fix[i][1] - fix[j][1]) ** 2
                )
                < ans + fix[j][2]
            ):
                return False
    return True


def meguru_bisect(ng, ok):
    """
    最小値を求める:
    (ng, ok) = (とり得る最小の値-1, とり得る最大の値+1)
    最大値を求める:
    (ng, ok) = (とり得る最大の値+1, とり得る最小の値-1)
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(L[mid]):
            ok = mid
        else:
            ng = mid
    return ok


# print(L)
print(L[meguru_bisect(len(L) - 1, 0)])
