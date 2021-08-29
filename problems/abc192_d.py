X = int(input())
M = int(input())

x = list(map(int, list(str(X))))
s = max(x)
lenx = len(x)
if lenx == 1:
    if X <= M:
        exit(print(1))
    else:
        exit(print(0))


def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    c = 0
    for i in range(lenx):
        c += x[lenx - i - 1] * (arg ** i)
        if c > M:
            return False
    return True


def meguru_bisect(ok, ng):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


# 文字型になっている
print(meguru_bisect(s, 10 ** 20) - s)
