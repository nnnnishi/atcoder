# https://qiita.com/drken/items/97e37dd6143e33a64c8c
# https://twitter.com/e869120/status/1377027868518064129
N, L = [int(_) for _ in input().split()]
K = int(input())
A = [int(_) for _ in input().split()] + [L]

# 長さansでいけるかどうかチェック
def is_ok(ans):
    k = 0
    tmp = 0
    for a in A:
        l = a - tmp
        if l >= ans:
            k += 1
            tmp = a
    if k >= K + 1:
        return True
    return False


def meguru_bisect(ng, ok):
    """
    最小値を求める:
    (ng, ok) = (とり得る最小の値-1, とり得る最大の値+1)
    最大値を求める:
    (ng, ok) = (とり得る最大の値+1, とり得る最小の値-1)
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(10 ** 16, 0))
