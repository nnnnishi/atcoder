S = list(input())
T = list(input())
N = len(S)
cnt = 0
for i in range(N - 1):
    if S[i] != T[i] and (S[i] == T[i + 1] and S[i + 1] == T[i]):
        for j in range(i + 2, N):
            if S[j] != T[j]:
                exit(print("No"))
        exit(print("Yes"))
    elif S[i] != T[i] and not (S[i] == T[i + 1] and S[i + 1] == T[i]):
        exit(print("No"))

if S[N - 1] == T[N - 1]:
    print("Yes")
else:
    print("No")
