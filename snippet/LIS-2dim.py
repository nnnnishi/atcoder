# 最長増加部分列(Longest Increase Subsequence)
# O(NlogN)
# https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/060.jpg
# https://atcoder.jp/contests/abc038/tasks/abc038_d
# https://pekempey.hatenablog.com/entry/2016/05/29/132404

# リストAからLISの長さを出す
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from operator import itemgetter

# 要素数
N = int(input())
# 探索対象の数列
A = []

for _ in range(N):
    w, h = [int(_) for _ in input().split()]
    A.append([w, h])

# 1キーwの昇順、2キーhの降順で並べて、hについてLISを探せばいい
A.sort(key=itemgetter(1), reverse=True)
A.sort(key=itemgetter(0))

# 部分列の長さと対応する値のindexに、最右の値を格納するためのDPテーブルを作る
dp = [A[0][1]]
P = [0] * N
P[0] = 1
for i in range(1, N):
    if A[i][1] > dp[-1]:
        # 一番大きいものより大きければ最後にその値を追加
        dp.append(A[i][1])
    else:
        # そうでないときは小さいところにその値を差し込む
        # それでも単調性は崩れない
        idx = bisect_left(dp, A[i][1])
        dp[idx] = A[i][1]

# 列の長さ
print(len(dp))
