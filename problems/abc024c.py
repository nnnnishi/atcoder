N, D, K = list(map(int, input().split()))
# LRの組をたしていく
DL = []
for i in range(D):
    L, R = list(map(int, input().split()))
    DL.append([L, R])
for i in range(K):
    S, T = list(map(int, input().split()))
    cnt = 0
    # みぎにすすむ
    if S <= T:
        for l, r in DL:
            cnt += 1
            if l <= S <= r and l <= T <= r:
                print(cnt)
                break
            elif l <= S <= r:
                S = r
    # ひだりにすすむ
    else:
        for l, r in DL:
            cnt += 1
            if l <= S <= r and l <= T <= r:
                print(cnt)
                break
            elif l <= S <= r:
                S = l
