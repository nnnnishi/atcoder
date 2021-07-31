import numpy as np

N, K = [int(_) for _ in input().split()]


def convert(n):
    """
    nをi進数からj進数へ変換
    """
    r = ""
    for s in list(str(np.base_repr(int(str(n), 8), base=9))):
        if s == "8":
            r += "5"
        else:
            r += s
    return int(r)


for i in range(K):
    N = convert(N)
print(N)