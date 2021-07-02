N, M = [int(_) for _ in input().split()]
L = []
R = []
S = []
A = [0] * (M + 2)
sumA = [0] * (M + 2)
ALLS = 0
for i in range(N):
    l, r, s = [int(_) for _ in input().split()]
    A[l] += s
    A[r + 1] -= s
    ALLS += s
    L.append(l)
    R.append(r)
    S.append(s)

minS = 10 ** 30
min_i = 0
for i in range(1, M + 1):
    sumA[i] = A[i] + sumA[i - 1]
    if sumA[i] <= minS:
        minS = sumA[i]
        min_i = i

for i in range(N):
    if L[i] <= min_i <= R[i]:
        ALLS -= S[i]
print(ALLS)