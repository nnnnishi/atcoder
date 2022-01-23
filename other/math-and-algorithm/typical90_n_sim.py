"""
参考
https://github.com/E869120/kyopro_educational_90/blob/main/editorial/014.jpg
"""
# 昇順でソート済みの重複ありの配列
A = [int(_) for _ in input().split()]
# 要素数
N = len(A)
# 右端、左端に余裕をもたせとく配列数は多くとも N - (右端の数A[N-1] - 左端の数A[0] + 1) で十分
M = N - (A[N - 1] - A[0] + 1)
# 余裕の数をM(最大値はN-1)として、左端と右端に余裕をつける,余裕が不要なら右端、左端は固定
if M > 0:
    B = [x for x in range(A[0] - M, A[N - 1] + M + 1)]
else:
    B = [x for x in range(A[0], A[N - 1] + 1)]

# Bのうち、最終的に利用する部分のリストCを用意
C = []
# O(N^2) で一番近いものに貪欲に紐付けて利用するBの箇所を特定, 1度Bの配列を利用したら使わない
used = set()
for a in A:
    diff = 10 ** 10
    idx = -1
    for b in B:
        if b not in used:
            diff_tmp = abs(b - a)
            if diff_tmp < diff:
                diff = diff_tmp
                idx = b
    C.append(idx)
    used.add(idx)

# 昇順にソート
C.sort()
# 答えのリスト
print(C)

# 差分計算（貪欲法：交差しないように左から順番に使う）
ans = 0
for a, c in zip(A, C):
    ans += abs(a - c)
print(ans)
