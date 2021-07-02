import numpy as np

R, X, Y = list(map(int, input().split()))


D = np.sqrt(X ** 2 + Y ** 2)
if D < R:
    print(2)
else:
    if D % R == 0:
        print(int(D // R))
    else:
        print(int((D // R) + 1))
