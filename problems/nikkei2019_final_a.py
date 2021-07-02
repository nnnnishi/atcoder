N = int(input())
A = [int(_) for _ in input().split()]
S = []
sumA = 0
for Ai in A:
    sumA += Ai
    S.append(sumA)

for k in range(N):
    tmp = S[k]
    for i in range(N - 1 - k):
        tmp = max(S[i + (k + 1)] - S[i], tmp)
    print(tmp)
