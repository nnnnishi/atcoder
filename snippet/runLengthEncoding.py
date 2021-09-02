import numpy as np


def RLE(sequence):
    (comp_seq_index,) = np.concatenate(
        ([True], sequence[1:] != sequence[:-1], [True])
    ).nonzero()
    return sequence[comp_seq_index[:-1]], np.ediff1d(comp_seq_index)

l = np.array(list("SSAAAAB"))
print(RLE(l))
