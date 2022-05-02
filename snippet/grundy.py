# https://www.creativ.xyz/grundy-number-1065/
def calc_grundy():
    W = 50
    B = 50
    # 追加する個数の最大値
    addB = W * (W + 1) // 2
    # すべてのw,bについてg[w][b] = 0
    g = [[0] * (B + addB + 1) for _ in range(W + 1)]
    # wが0から小さい順にgrundy数を計算
    for w in range(W + 1):
        for b in range(addB + 1):
            # あるw,bについて
            mex = [0] * (B + addB + 1)
            # wを1減らしてbをwたすのは手数が1増える
            if w >= 1:
                # w-1については計算済み、w - 1,bのgrundy数は追加で1手かかり0にはならない
                mex[g[w - 1][b + w]] = 1
            # bが2以上ある場合はwそのままで割れなくなるまでは手数が0より大きくなる
            if b >= 2:
                for k in range(1, b // 2 + 1):
                    # w, b-kについては計算済み、w - 1,w + bのgrundy数は追加で1手かかり0にはならない
                    mex[g[w][b - k]] = 1
            for k in range(B + addB + 1):
                # mexが0となる最小のkがgrundy数
                if mex[k] == 0:
                    g[w][b] = k
                    break
    return g


N = int(input())
W = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
g = calc_grundy()
count = 0
for w, b in zip(W, B):
    count ^= g[w][b]

if count == 0:
    print("Second")
else:
    print("First")
