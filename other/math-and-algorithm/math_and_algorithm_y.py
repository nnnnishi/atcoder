import numpy as np

N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
print(np.sum(B) * 2 / 3 + np.sum(A) / 3)
