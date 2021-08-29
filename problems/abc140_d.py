N, K = [int(_) for _ in input().split()]
S = list(input())

import numpy as np


def RLE(sequence):
    (comp_seq_index,) = np.concatenate(
        ([True], sequence[1:] != sequence[:-1], [True])
    ).nonzero()
    return sequence[comp_seq_index[:-1]], np.ediff1d(comp_seq_index)


S = RLE(np.array(S))
gr = len(S[0])
for i in range(K):
    if gr >= 3:
        gr -= 2
    elif gr == 2:
        gr = 1
print(N - gr)
