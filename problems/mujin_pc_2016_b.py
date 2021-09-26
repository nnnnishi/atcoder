import numpy as np

A, B, C = [int(_) for _ in input().split()]
if A > (B + C):
    d = (A + B + C) ** 2 - (A - (B + C)) ** 2
elif B > (A + C):
    d = (A + B + C) ** 2 - (B - (A + C)) ** 2
elif C > (A + B):
    d = (A + B + C) ** 2 - (C - (A + B)) ** 2
else:
    d = (A + B + C) ** 2
print(d * np.pi)
