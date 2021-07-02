N, Q = [int(_) for _ in input().split()]
S = input()
LR = []
for _ in range(Q):
    l, r = [int(_) for _ in input().split()]
    LR.append([l, r])
sumAC = [0] * len(S)
for i in range(1, len(S)):
    if S[i - 1] + S[i] == "AC":
        sumAC[i] = sumAC[i - 1] + 1
    else:
        sumAC[i] = sumAC[i - 1]
for l, r in LR:
    print(sumAC[r - 1] - sumAC[l - 1])
