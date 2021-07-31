N, L = [int(_) for _ in input().split()]
K = int(input())
A = [0] + [int(_) for _ in input().split()] + [L]


def is_ok(t):
    # 条件を満たすかどうか？問題ごとに定義
    # t以上のものだけでKつくれるか
    b = 0
    c = 0
    for i in range(1, N + 2):
        c += A[i] - A[i - 1]
        if c >= t:
            b += 1
            c = 0
    if b > K:
        return True
    else:
        return False


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


print(meguru_bisect(0, 10 ** 9 + 1))
