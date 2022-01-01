import numpy as np

N = int(input())
ans = 0
for i in range(N):
    p, q = [int(_) for _ in input().split()]
    ans += q / p
print(ans)
