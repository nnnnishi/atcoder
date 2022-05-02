import pprint


def gaussian_elimination_xor(A, see_last_col=True):
    H = len(A)
    W = len(A[0])
    rank = 0
    for w in range(W):
        if not see_last_col:
            if w == W - 1:
                break
        for h in range(rank, H):
            if A[h][w]:
                if h != rank:
                    A[h], A[rank] = A[rank], A[h]
                for hh in range(H):
                    if hh != rank:
                        if A[hh][w]:
                            for ww in range(W):
                                A[hh][ww] ^= A[rank][ww]
                rank += 1
                break
    return A, rank


# N:行、M:列
N, M = map(int, input().split())
mod = 998244353

A = [[0] * (N + 1) for _ in range(M)]
for i in range(N):
    t = int(input())
    a = list(map(int, input().split()))
    # i行目、j列目を1に反転
    for j in a:
        A[j - 1][i] = 1
s = list(map(int, input().split()))
for i in range(M):
    # 最後の行の列をsに合わせる
    A[i][-1] = s[i]
# pprint.pprint(A, width=50)
A, rank = gaussian_elimination_xor(A, False)
# pprint.pprint(A, width=50)
# print(rank)
for i in range(rank, M):
    if A[i][-1]:
        print(0)
        exit()
# rank分で自由に調整できれば残りのN-rank分は自由に動かしてよい-> 2^(N-rank)
print(pow(2, N - rank, mod))
