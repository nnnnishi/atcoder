# 最長増加部分列(Longest Increase Subsequence)
# O(NlogN)
# https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/060.jpg

# リストAからLISの長さを出す
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort

# 要素数
N = int(input())
# 探索対象の数列
A = [int(_) for _ in input().split()]

# 部分列の長さと対応する値のindexに、最右の値を格納するためのDPテーブルを作る
dp = [A[0]]
P = [0] * N
P[0] = 1
for i in range(1, N):
    if A[i] > dp[-1]:
        # 一番大きいものより大きければ最後にその値を追加
        dp.append(A[i])
        # ちょうどiまでのLISはそのときのdpの長さ
        P[i] = len(dp)
    else:
        # そうでないときは小さいところにその値を差し込む
        # それでも単調性は崩れない
        idx = bisect_left(dp, A[i])
        dp[idx] = A[i]
        # ちょうどiまでのLISは差し込んだidxの値+1 (0-indexなので)
        P[i] = idx + 1

# 列の長さ
print(len(dp))
