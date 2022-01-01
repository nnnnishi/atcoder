import numpy as np

N = int(input())
ans = 0
for i in range(N):
    ans += N / (N - i)
print(ans)
