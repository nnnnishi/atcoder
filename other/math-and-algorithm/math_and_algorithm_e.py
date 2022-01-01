import numpy as np

N = int(input())
A = [int(_) for _ in input().split()]
print(np.sum(A) % 100)
