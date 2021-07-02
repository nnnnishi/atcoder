import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

M, N = map(int, readline().split())
K = int(readline())
grid = np.zeros((M + 1, N + 1), "S1")
for i in range(1, M + 1):
    grid[i, 1:] = np.frombuffer(readline().rstrip(), "S1")

query = np.array(read().split(), np.int32)

J = (grid == b"J").cumsum(axis=0).cumsum(axis=1)
O = (grid == b"O").cumsum(axis=0).cumsum(axis=1)

A = query[::4] - 1
B = query[1::4] - 1
C = query[2::4]
D = query[3::4]

J = J[C, D] + J[A, B] - J[C, B] - J[A, D]
O = O[C, D] + O[A, B] - O[C, B] - O[A, D]
I = (C - A) * (D - B) - J - O

print("\n".join("{} {} {}".format(j, o, i) for j, o, i in zip(J, O, I)))
