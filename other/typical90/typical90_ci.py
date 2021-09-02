N, P, K = [int(_) for _ in input().split()]
a = []
for _ in range(N):
    a.append(input())


def wf(X):
    global a
    dist = []
    for ai in a:
        dist.append(list(map(int, ai.replace("-1", str(X)).split())))
    # ワーシャルフロイド
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    c = 0
    for i in range(N):
        for j in range(i + 1, N):
            if dist[i][j] <= P:
                c += 1
    return c


# Kの上限
def meguru_large(ok, ng):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if wf(mid) > K:
            ok = mid
        else:
            ng = mid
    return ok


# Kの下限
def meguru_small(ok, ng):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if wf(mid) >= K:
            ok = mid
        else:
            ng = mid
    return ok


INF = 10 ** 9 + 1
check = wf(INF)
# print(check)
if check == K:
    print("Infinity")
elif check > K:
    print(0)
else:
    l = meguru_large(0, INF)
    s = meguru_small(0, INF)
    # print(s, l)
    print(s - l)
