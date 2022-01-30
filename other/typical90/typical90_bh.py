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

# 左側からの増加列
# 部分列の長さと対応する値のindexに、数列の最終要素の最小値を格納するためのDPテーブルを作る
dp = [A[0]]
P = [0] * N
Q = [0] * N
P[0] = 1
Q[N - 1] = 1
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

# 右側からの増加列
# 部分列の長さと対応する値のindexに、数列の最終要素の最小値を格納するためのDPテーブルを作る
dp2 = [A[N - 1]]
for i in range(N - 2, -1, -1):
    if A[i] > dp2[-1]:
        # 一番大きいものより大きければ最後に追加
        dp2.append(A[i])
        # ちょうどiまでのLISはそのときのdpの長さ
        Q[i] = len(dp2)
    # そうでないときは小さいところにその値を差し込む
    # それでも単調性は崩れない
    else:
        idx = bisect_left(dp2, A[i])
        dp2[idx] = A[i]
        # ちょうどiまでのLISは差し込んだidxの値+1 (0-indexなので)
        Q[i] = idx + 1

ans = 0
for i in range(N):
    # 両端からのLISは、 左からのLIS+右からのLIS-そのidx分1
    if P[i] + Q[i] - 1 > ans:
        ans = P[i] + Q[i] - 1
print(ans)
