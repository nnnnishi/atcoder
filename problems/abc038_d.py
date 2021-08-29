N = int(input())
a = []
for i in range(N):
    w, h = [int(_) for _ in input().split()]
    a.append((w, h))
a.sort(key=lambda x: (x[0], -x[1]))


import bisect

seq = [x[1] for x in a]

LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

# 列の長さ
print(len(LIS))