from copy import deepcopy

H, W, K = [int(_) for _ in input().split()]
C = []
for i in range(H):
    C.append([int(_) for _ in list(input())])

# 落とす処理
def drop():
    # 左下から右上のセルへ
    for y in range(H - 1, 0, -1):
        for x in range(W):
            # 上が0でなく下が0のとき、落とす（yが上ほど...）
            if C[y][x] == 0 and C[y - 1][x] != 0:
                # 最初のセルのy、下のやつ
                k = y
                # 一番上に0を運ぶ
                while k < H and C[k][x] == 0:
                    # 下のセルに上のセルをコピー
                    C[k][x] = C[k - 1][x]
                    # 上のセルは0
                    C[k - 1][x] = 0
                    # ひとつ下みる
                    k += 1


# 揃ったところを消して合計を計算
def check(times):
    # 合計得点
    sm = 0
    for y in range(H):
        # 確認する始点
        st = 0
        cnt = 1
        for x in range(1, W):
            # 隣り合うのが同じなら+1
            if C[y][x - 1] == C[y][x]:
                cnt += 1
            else:
                # 隣り合うのが同じでなくcntがK以上たまったときは処理
                if cnt >= K:
                    # 消す個数をたす
                    sm += C[y][x - 1] * cnt
                    # 始点からx-1まで同じなので0にして消す
                    for k in range(st, x):
                        C[y][k] = 0
                # 隣接が同じcntを初期化
                cnt = 1
                # 始点を初期化
                st = x
        # 最後に隣接が同じものが残っていたら消す
        if cnt >= K:
            sm += C[y][x] * cnt
            for k in range(st, x + 1):
                C[y][k] = 0
    return 2 ** times * sm


# 　最初
cc = deepcopy(C)
ans = 0
for i in range(H):
    for j in range(W):
        # 元の状態は保持しておいて、全部試す
        C = deepcopy(cc)
        C[i][j] = 0
        res = 1
        score = times = 0
        # 消えるところがある限りループ
        while res:
            drop()
            res = check(times)
            score += res
            times += 1
        ans = max(ans, score)
print(ans)