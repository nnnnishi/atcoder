S = list(input())
N = len(S)
T = S.copy()
idx = 0
for i in range(N - 1, -1, -1):
    if i <= idx:
        print("Yes")
        exit()
    if S[i] == "a":
        if T[idx] == "a":
            idx += 1
    else:
        if T[idx] == S[i]:
            idx += 1
        else:
            print("No")
            exit()

