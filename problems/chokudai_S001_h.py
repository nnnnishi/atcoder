# 最長増加部分列(longest increase subsequence)
# https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/060.jpg

# リストseqからLISの長さを出す

import bisect

N = int(input())
seq = [int(_) for _ in input().split()]

LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

# 列の長さ
print(len(LIS))