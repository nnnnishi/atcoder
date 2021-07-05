# 最小公約数
import math

N = int(input())
A = [int(_) for _ in input().split()]
L = [A[0]]
R = [A[N - 1]]
for i in range(1, N):
    L.append(math.gcd(L[i - 1], A[i]))
    R.append(math.gcd(R[i - 1], A[N - 1 - i]))
invR = R[::-1]
ans = max(invR[1], L[N - 2])
for i in range(N - 2):
    ans = max(ans, math.gcd(L[i], invR[i + 2]))
print(ans)