import numpy as np

N = int(input())
B = [int(_) for _ in input().split()]
R = [int(_) for _ in input().split()]
print(np.mean(B) + np.mean(R))
