import numpy as np

R, C = [int(_) for _ in input().split()]
a = [[int(_) for _ in input().split()] for i in range(R)]
a = np.array(a)


def has_bit(n, i):
    return (n & 1 << i) > 0


ans = 0
b = a.copy()
for n in range(1 << R):
    for i in range(R):
        if has_bit(n, i):
            b[i] = (a[i] ^ 1).copy()
        else:
            b[i] = a[i].copy()
    tmp_ans = 0
    for j in np.sum(b, axis=0):
        if j >= (R + 1) // 2:
            tmp_ans += j
        else:
            tmp_ans += R - j
    ans = max(tmp_ans, ans)
print(ans)