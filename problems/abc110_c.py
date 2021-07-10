R1 = {}
R2 = {}

S = list(input())
T = list(input())
for i in range(len(S)):
    if S[i] in R1:
        if R1[S[i]] == T[i]:
            continue
        else:
            exit(print("No"))
    else:
        R1[S[i]] = T[i]
    if T[i] in R2:
        if R2[T[i]] == S[i]:
            continue
        else:
            exit(print("No"))
    else:
        R2[T[i]] = S[i]
print("Yes")
