# 最長増加部分列(longest increase subsequence)
# O(NlogN)
# https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/060.jpg
import bisect
# リストseqからLISの長さを出す
N = int(input())
seq = []
for i in range(N):
    seq.append(int(input()))

LIS = [-seq[0]]
for i in range(1,len(seq)):
    if -seq[i] >= LIS[-1]:
        LIS.append(-seq[i])
    else:
        LIS[bisect.bisect_right(LIS, -seq[i])] = -seq[i]
    #print(LIS)
# 列の長さ
print(len(LIS))
