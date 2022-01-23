import sys

input = sys.stdin.readline

N = int(input())
P = [int(_) for _ in input().split()]
Q = [int(_) for _ in input().split()]
d = {}
for i in range(N):
    d[Q[i]] = i

a = []
for i, p in enumerate(P):
    mut = p
    b = []
    while mut <= N:
        b.append(d[mut])
        mut += p
    b.sort(reverse=True)
    for bi in b:
        a.append((i, bi))


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
